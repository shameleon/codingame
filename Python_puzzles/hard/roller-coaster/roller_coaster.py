from collections import deque 
import sys
import math


class AttractionState:
    """a given index of the group queue is associated
    with the number of people that can ride the attraction."""
    def __init__(self, idx, load):
        self.first_group_idx = idx
        self.load = load


class RollerCoaster:
    """The attraction contains a maximal load and count of rotation.
    the groups are in a queue. The initial index is watched to identify 
    states of the queue"""
    def __init__(self, l, c, n):
        self.p = {'load': l, 'count': c, 'groups': n}
        self.q = deque()
        [self.q.append(int(input())) for i in range(n)]
        self.income = 0
        self.idx = deque()
        [self.idx.append(i) for i in range(n)]
        self.states = []
        self.loop = {}
        self.turn = 0

    def _find_previous_state(self, head_idx):
        """if a previous state is found again, the following states
        are going to happen again"""
        loads = 0
        rides = -1
        for state in self.states:
            if state.first_group_idx == head_idx:
                rides = 0
            if rides >= 0:
                if self.turn + rides < self.p['count']:
                    rides += 1
                    loads += state.load
                else:
                    break
        return rides, loads

    def _load_a_ride(self):
        """ groups from the deque arre added 
        until the attraction is fully loaded with people.
        groups index queues are rotated (popleft and append)
        the index of the initial group at the head of the queue 
        and the final loaded number of people are stored for an
        eventual further encoutering.
        """
        load = 0
        groups_in = 0
        head_idx = self.idx[0]
        while groups_in < self.p['groups']:
            if load + self.q[0] <= self.p['load']:
                load += self.q[0]
                self.q.rotate(-1)
                self.idx.rotate(-1)
                groups_in += 1
            else:
                break
        self.states.append(AttractionState(head_idx, load))
        return load

    def daily_income(self):
        """Attraction daily income calculation is based on 
        the C number of daily rotations.
        For each rotation, 
            _load_a_ride() to maximize groups of people in the attraction
            _find_previous_state() if the current state has been previously found
        """
        income = 0
        self.turn = 0
        while self.turn < self.p['count']:
            rides, loads = self._find_previous_state(self.idx[0])
            if rides > 0:
                income += loads
                self.turn += rides
                self.loop[self.idx[0]] = [rides, loads]
            else:
                income += self._load_a_ride()
                self.turn += 1
        print(income)


def main():
    """The attraction contains a limited number L of places.
    The attraction can only function C number of times per day.
    The queue contains a number N of groups.
    Each group contains a number Pi of people.
    Each person spends 1 dirham per ride."""
    l, c, n = [int(i) for i in input().split()]
    print(l,c,n, file=sys.stderr, flush=True)
    roller_coaster = RollerCoaster(l, c, n)
    roller_coaster.daily_income()


if __name__ == "__main__":
    main()
