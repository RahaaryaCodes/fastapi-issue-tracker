from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class IssueStatus(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"


class IssuePriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class IssueCreate(BaseModel):
    title: str = Field(..., example="Sample Issue")
    description: Optional[str] = Field(
        None, example="This is a sample issue description.")
    status: IssueStatus = Field(IssueStatus.OPEN, example=IssueStatus.OPEN)
    priority: IssuePriority = Field(
        IssuePriority.MEDIUM, example=IssuePriority.MEDIUM)


class IssueUpdate(BaseModel):
    title: Optional[str] = Field(None, example="Updated Issue Title")
    description: Optional[str] = Field(
        None, example="Updated issue description.")
    status: Optional[IssueStatus] = Field(
        None, example=IssueStatus.IN_PROGRESS)
    priority: Optional[IssuePriority] = Field(
        None, example=IssuePriority.HIGH)


class IssueOutput(BaseModel):
    id: str
    title: str
    description: Optional[str]
    status: IssueStatus
    priority: IssuePriority


class issueDelete(BaseModel):
    id: str
