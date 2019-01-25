# TimingAlfred

[Alfred 3 workflow](https://www.alfredapp.com/workflows/) to search and create tasks in [Timing](https://timingapp.com/).
[Original Repo](https://github.com/elony314/alfred-timing)

## Usage
`tmt` -- List the recent taks or search for a specific task to start it. 

`tms` -- Stop the current task. 

## Thanks
- [chrisbro](https://github.com/chrisbro): use his [alfred-bear](https://github.com/chrisbro/alfred-bear) as the skeleton.

## Reference

* Alfred Workflows Help: https://www.alfredapp.com/help/workflows/
* Timing Site Applescript reference: https://timingapp.com/help/applescript
* Timing Starting and stopping a Task Applescript: 
``` Applescript
    -- Copyright (c) 2017 timingapp.com / Daniel Alm. All rights reserved.
    -- This script is licensed only to extend the functionality of Timing. Redistribution and any other uses are not allowed without prior permission from us.
    tell application "TimingHelper"
        set pr to front project whose name is "ProjectXYZ"
        start task with description "What you were doing" project pr for about 3600
        -- and later:
        stop current task with notification  -- if you don't want Timing to display a notification about the stopped task, remove the 'with notification'
    end tell
```
* Timing Pause Tracking Applescript:

``` Applescript
    -- Copyright (c) 2017 timingapp.com / Daniel Alm. All rights reserved.
    -- This script is licensed only to extend the functionality of Timing. Redistribution and any other uses are not allowed without prior permission from us.
    tell application "TimingHelper"
        pause tracking
        delay 5 * 60
        resume tracking
    end tell
```

* Timing Control Tracking Applescript: 

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
- [X] Quick Start task (list tasks)
- [ ] Pause task
- [ ] Open Review window

[![Waffle.io - Columns and their card count](https://badge.waffle.io/lisaross/TimingAlfred.svg?columns=all)](https://waffle.io/lisaross/TimingAlfred)
