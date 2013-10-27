from unittest import TestCase
from dataDAO import TimesheetEntry, TimesheetDAO, MemoryTimesheetDAOImpl
from datetime import datetime

__author__ = 'andrewr'


class TestTimesheetDAO(TestCase):

    def setUp(self):
        self._dao = TimesheetDAO(MemoryTimesheetDAOImpl())

    def test_single_add(self):
        entry = TimesheetEntry(1, datetime(2013, 12, 11, 9, 34, 12))

        self._dao.store(entry)
        self.assertEqual(len(self._dao.fetch_all()), 1)
