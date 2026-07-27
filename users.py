
from fastapi import Depends, HTTPException, status

from models import User, Role
from security_utilities import get_current_user


def admin_only( current_user: User = Depends(get_current_user)):

    if current_user.role != Role.admin:

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )

    return current_user


def admin_or_employee(
    current_user: User = Depends(get_current_user)
):

    if current_user.role not in [
        Role.admin,
        Role.employee
    ]:

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admin or employee can perform this operation."
        )

    return current_user