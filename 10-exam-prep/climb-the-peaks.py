from collections import deque

peaks_to_climb: dict[int, str] = {
    80: "Vihren",
    90: "Kutelo",
    100: "Banski Suhodol",
    60: "Polezhan",
    70: "Kamenitza"
}

total_peaks = len(peaks_to_climb)
climbed_peaks: list[str] = []
food_supplies = [int(x) for x in input().split(', ')]
stamina_deque = deque([int(x) for x in input().split(', ')])

while food_supplies and stamina_deque:
    last_food = food_supplies.pop()
    first_stamina = stamina_deque.popleft()

    total = last_food + first_stamina

    if peaks_to_climb:
        for points, peak in peaks_to_climb.items():
            if total >= points:
                climbed_peaks.append(peak)
                peaks_to_climb.pop(points)
            break

if len(climbed_peaks) == total_peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if climbed_peaks:
    print("Conquered peaks:")
    for peak in climbed_peaks:
        print(peak)
