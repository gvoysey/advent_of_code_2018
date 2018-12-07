from aoc.utils import load
import pendulum
import attr
from enum import Enum, auto
import re


class State(Enum):
    AWAKE = auto()
    ASLEEP = auto()


@attr.s(cmp=True)
class LogRecord:
    timestamp = attr.ib()
    state = attr.ib()
    guard_id = attr.ib(default=None)


def parse_line(line: str):
    date_str = re.findall(r'\[(.*)\]', line)[0]
    is_asleep = "falls asleep" in line
    try:
        guard_id = int(re.findall(r'Guard #(\d*)', line)[0])
        return LogRecord(timestamp=pendulum.parse(date_str),
                         guard_id=guard_id,
                         state=State.ASLEEP if is_asleep else State.AWAKE)
    except IndexError:
        return LogRecord(timestamp=pendulum.parse(date_str),
                         state=State.ASLEEP if is_asleep else State.AWAKE)


def main(infile):
    logfile = load(infile)
    unsorted = [parse_line(x) for x in logfile]
    time_log = sorted(unsorted, key=lambda x: x.timestamp)

    curr_guard = None
    for log in time_log:
        if log.guard_id:
            curr_guard = log.guard_id
        else:
            log.guard_id = curr_guard

    sleep_log = {}
    for log in time_log:
        if log.state == State.AWAKE

if __name__ == "__main__":
    main('input.txt')