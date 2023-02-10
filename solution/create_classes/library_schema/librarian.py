# -*- coding: utf-8 -*-
"""
Librarian Class
----------------------

Code for creating ORM Class
"""
import logging

from sqlalchemy import Column, VARCHAR
from sqlalchemy.orm import relationship

from solution.base_class import AuditAttributesMixin, Base

__author__ = "neelesh.karthi@gmail.com"

LOGGER = logging.getLogger(name=__name__)


class Librarian(AuditAttributesMixin, Base):
    """
    Librarian class docstring

    :ivar pk_id: pk_id
    :vartype pk_id: int

    :ivar name: name
    :vartype name: str

    :ivar created_by: user name of creator
    :vartype created_by: str

    :ivar created_on: timestamp while creating
    :vartype created_on: :class:`datetime.datetime`

    :ivar last_updated_by: user name of updater
    :vartype last_updated_by: str

    :ivar last_updated_on: timestamp while updating
    :vartype last_updated_on: :class:`datetime.datetime`

    :ivar is_active: active status
    :vartype is_active: bool

    """
    __tablename__ = "librarian"

    name = Column(VARCHAR(255), nullable=False)

    # relationship
    staff_activity = relationship("StaffActivity", back_populates="librarian")
    student_activity = relationship("StudentActivity", back_populates="librarian")

    def __init__(self, name):
        """
        creates an instance of the class

        :param name: name
        :type name: str
        """
        self.name = name

        LOGGER.debug("Created %s (Librarian Object)", name)
