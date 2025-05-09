from Machine import Machine

if __name__ == "__main__":
    machine = Machine()

    # Machine starts in IdleState, then it transitions to ActiveState
    machine.handle()  # Machine is currently idle. Switching to active state.

    # Machine now in ActiveState, transitions to MaintenanceState
    machine.handle()  # Machine is active. Switching to maintenance state.

    # Machine now in MaintenanceState, transitions to ErrorState
    machine.handle()  # Machine is under maintenance. Switching to error state.

    # Machine now in ErrorState, transitions to IdleState
    machine.handle()  # Machine is in error state. Resetting to idle.
