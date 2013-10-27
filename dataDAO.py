"""
Interface for DAO operations to store/retrieve timesheet data
"""

from datetime import datetime


class TimesheetDAO:

    def __init__(self, impl):
        self.impl = impl

    def store(self, entry):
        """ Store a single entry. Overwrite entry with same timestamp """
        return self.impl.store(entry)

    def fetch_all(self):
        """ Fetch all TimesheetEntry objects """
        return self.impl.fetch_all()

    def fetch(self, fromd, tod):
        """ Fetch all TimesheetEntry objects within a time range (time ordered) """
        return self.impl.fetch(fromd, tod)

    def delete(self, entry_id):
        """ Delete a single entry by id. Return true if anything deletedm false otherwise"""
        return self.impl.delete(entry_id)

    def delete_range(self, fromd, tod):
        """ Remove all TimesheetEntry objects within a time range """
        return self.impl.delete(fromd, tod)


class MemoryTimesheetDAOImpl:
    """ In-memory implementation of DAO Impl for testing"""

    def __init__(self):
        self._data = []

    def store(self, entry):
        # delete entries with same timestamp first
        self._data[:] = [tup for tup in self._data if tup.timestamp != entry.timestamp]
        self._data.append(entry)

    def fetch_all(self):
        return sorted(self._data)

    def fetch(self, fromd, tod):
        retlist = []
        for entry in self._data:
            if (entry.timestamp >= fromd) and (entry.timestamp <= tod):
                retlist.append(entry)
        return sorted(retlist)

    def delete(self, entry_id):
        beforelen = len(self._data)
        self._data[:] = [tup for tup in self._data if tup.entry_id != entry_id]
        return len(self._data) != beforelen

    def delete_range(self, fromd, tod):
        beforelen = len(self._data)
        self._data[:] = [tup for tup in self._data if (tup.timestamp >= fromd) and (tup.timestamp <= tod)]
        return len(self._data) != beforelen


class TimesheetEntry:

    def __init__(self, entry_id = -1, timestamp=datetime.now(), activity="UNKNOWN"):
        self.entry_id = entry_id
        self.timestamp = timestamp
        self.activity = activity

    def __repr__(self):
        return self.timestamp.isoformat() + ' ' + self.activity + str(self.entry_id)
