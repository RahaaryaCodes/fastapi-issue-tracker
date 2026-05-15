import uuid
from fastapi import APIRouter, HTTPException, status
from app.schemas import IssueCreate, IssueUpdate, IssueOutput
from app.storage import load_issues, save_issues

router = APIRouter(prefix="/api/v1/issues", tags=["issues"])


@router.get("/", response_model=list[IssueOutput])
async def get_issues():
    issues = load_issues()
    return [IssueOutput(**issue) for issue in issues]


@router.post("/", response_model=IssueOutput, status_code=status.HTTP_201_CREATED)
async def create_issue(issue: IssueCreate):
    issues = load_issues()
    new_issue = issue.model_dump()
    new_issue["id"] = str(uuid.uuid4())
    issues.append(new_issue)
    save_issues(issues)
    return IssueOutput(**new_issue)


@router.get("/{issue_id}", response_model=IssueOutput)
async def get_issue(issue_id: str):
    issues = load_issues()
    for issue in issues:
        if issue["id"] == issue_id:
            return IssueOutput(**issue)
    raise HTTPException(status_code=404, detail="Issue not found")


@router.put("/{issue_id}", response_model=IssueOutput)
async def update_issue(issue_id: str, issue_update: IssueUpdate):
    issues = load_issues()
    for index, issue in enumerate(issues):
        if issue["id"] == issue_id:
            updated_issue = issue.copy()
            update_data = issue_update.model_dump(exclude_unset=True)
            updated_issue.update(update_data)
            issues[index] = updated_issue
            save_issues(issues)
            return IssueOutput(**updated_issue)
    raise HTTPException(status_code=404, detail="Issue not found")


@router.delete("/{issue_id}")
async def delete_issue(issue_id: str):
    issues = load_issues()

    for issue in issues:
        if issue["id"] == issue_id:
            issues.remove(issue)

            save_issues(issues)

            return {"message": "Issue deleted successfully"}

    raise HTTPException(status_code=404, detail="Issue not found")
