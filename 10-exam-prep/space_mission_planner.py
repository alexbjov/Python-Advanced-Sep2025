def check_mission_feasibility(max_crew_size, total_budget, *args):
    confirmed = []
    suspended = []
    total_missions = len(args)

    for mission_name, required_crew_size, mission_budget in args:
        if required_crew_size <= max_crew_size and mission_budget <= total_budget:
            confirmed.append((mission_name, required_crew_size, mission_budget))
            total_budget -= mission_budget
        else:
            suspended.append((mission_name, required_crew_size, mission_budget))

    result = []
    if len(confirmed) == total_missions:
        result.append("All missions are feasible within crew and budget limits.")

    if confirmed:
        sorted_confirmed_missions = sorted(confirmed, key=lambda x: x[0])
        result.append("Confirmed Missions:")
        for mission, crew_size, budget in sorted_confirmed_missions:
            result.append(f"${mission}, crew size: {crew_size}, budget: {budget:.2f}")

    if suspended:
        sorted_suspended_missions = sorted(suspended, key=lambda x: (-x[1], -x[2]))
        result.append("Suspended Missions:")
        for mission, crew_size, budget in sorted_suspended_missions:
            result.append(f"!{mission}, crew size: {crew_size}, budget: {budget:.2f}")

    return "\n".join(result)

# print(check_mission_feasibility(
#     5, 100_000_000.0,
#     ("Apollo 11", 3, 10_000_000.0),
#     ("Voyager 1", 2, 5_000_000.0),
#     ("Hubble 2", 4, 8_000_000.0)
# ))

# print(check_mission_feasibility(
#     3, 9_000_000.0,
#     ("Apollo 11", 3, 9_000_000.1),
#     ("Voyager 1", 2, 5_000_000.0),
#     ("Hubble 2", 4, 3_000_000.0),
#     ("Lunar 5", 3, 9_000_001.0)
# ))

# print(check_mission_feasibility(
#     4, 9_000_000.0,
#     ("Apollo 11", 5, 2_000_000.1),
#     ("Voyager 1", 5, 1_000_000.0),
#     ("Hubble 2", 4, 9_000_000.01),
#     ("Lunar 5", 8, 500_000.0)
# ))

# print(check_mission_feasibility(
#     3, 20_000_000.0,
#     ("Voyager 1", 2, 5_000_000.0),
#     ("Hubble 2", 4, 3_000_000.0),
#     ("Lunar 4", 3, 6_000_001.0),
#     ("Apollo 11", 3, 9_000_000.1),
#     ("Hubble 3", 4, 2_000_000.0),
#     ("Lunar 5", 3, 4_000_001.0)
# ))
