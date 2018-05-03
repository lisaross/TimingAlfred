# TimingAlfred
Alfred workflows for Timing (timingapp.com)

Note: haven't started. This is just a scratch file for what I want to do.

## Reference

* Alfred Workflows Help: https://www.alfredapp.com/help/workflows/
* Timing Applescript: 

``` Applescript
    -- Copyright (c) 2017 timingapp.com / Daniel Alm. All rights reserved.
    -- This script is licensed only to extend the functionality of Timing. Redistribution and any other uses are not allowed without prior permission from us.
    set datevar to current date
    set hours of datevar to 7
    set minutes of datevar to 0
    set seconds of datevar to 0

    tell application "TimingHelper"
	add task from ((datevar)) to ((datevar) + 1 * hours) with description "foo" project (front project whose name is "ProjectXYZ")
        -- note: if there are two projects with the same names, but different parent projects, you can address them as follows:
        -- front project whose name chain is "Parent1 ▸ Child"
        -- front project whose name chain is "Parent2 ▸ Child"
    end tell
```

## Todo

- [ ] Add task
- [ ] Quick Start task (list tasks)
- [ ] Pause task
- [ ] Open Review window

[![Waffle.io - Columns and their card count](https://badge.waffle.io/lisaross/TimingAlfred.svg?columns=all)](https://waffle.io/lisaross/TimingAlfred)
