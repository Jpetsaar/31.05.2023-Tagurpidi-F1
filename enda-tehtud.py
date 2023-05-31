"""
kirjuta funktsioon ,mis arvutab juhusliku aja etteantud
vahemikus. Vahemik on sekundites ja kaasa arvatud.Lõpp
tulemusena näitab lisaks sekundile ja tuhandikke. Näiteks:
Kui vahemik on 47-59 sekundit, siis juhuslik aeg on 52.432 sekundit.
siis juhuslik aeg on 52.432 sekundit.
Tee list viie eesnimega kes võistlevad. Genereeri igale ühele
kolm sektori aega vahemikus 23 kuni 26 k.a. Väljasta iga isiku järgi
kolm aega.

Näiteks:
Lewis 25.12 25.286 25.935
Valtteri 25.96 26.858 26.993

Väljasta ajad ühel joonel. Nime max pikkus on 10 märki. Näiteks:
Lewis      25.12 25.286 25.935
Valtteri   25.96 26.858 26.993

Kõige esimeseks tuleb kogu aeg ja siis s1,s2,s3.
Lewis     72.778  25.12 25.286 25.935
Valtteri  77.952  25.96 26.858 26.993

Kogu aeg vormindada kujule 00:00:00.000 ehk 77.987 => 00:01:17.987
Lewis    00:01:15.414  25.12 25.286 25.935
Valtteri 00:01:12.485  25.96 26.858 26.993

Kirjuta funktsioon, mis arvutab täisringi aja kasutades esimeses
punktis tehtud funktsiooni  uue funktsiooni sees! Aegade vahemik
sektorites on sama ,mis alguses(23 ja 26). Sektori aeg sel korral
meeles pidama ei pea. Ainult täisringi aeg.

Nüüd kui on peaaegu kogu vajalik info olemas tuleb teha "Võistlus"
Võistlus on 10 ringi .Meeles tuleb pidada igal ringil sõitja aega(ringi)
ja kogu aega (sisse sõidetud ringinde summa ).Kogu info peab olema listis (nimi ja sõidetud ringide summa )
Kogu info peab olema listis (nimi ja sõidetud ringide aegade summa ). Kui info olemas näita lõpus lõpp tulemust.
Ära unusta listi sorteerida aja järgi kasvavalt.

Valtteri    00:08:18.204
Lewis       00:08:27.252

Võistlusel on ikka nii ,et kõik ringid ei tule hästi välja. Seega
mõnel ringil võiks juhtuda äpardus. See tähendab, et sektori aeg
poleks enam 23 ja 26 sek., vahel vaid 30 ja 90 sek. vahel ka. Enne
ringi aja arvutamist tehke lihtne loogiline kontroll. Genereerige
juhuslik number vahemikus 1-10 või 0-9 ja kui see number on 2,
siis juhtus midagi ja arvutage sektori aeg nüüd vahemikus 30-90 k.a.
Lewis       00:09:11.433
Valtteri    00:12:36.756

Sõit ja kõik "koperdamised" pane listi - ringi number. Ja kui
väljastatakse sõitja info, siis näita ringi numbreid kasutaja järgi.
Valtteri  00:08:17.793
Lewis     00:10:10.002 7 10

VÕI

Valtteri  00:08:17.793 []
Lewis     00:10:10.002 [7, 10]

Arvuta alates teisest sõitjast vahe esimesega. Aega näita
põhiaja järgi enne vigaseid ringide numbreid näiteks:
Evelin    00:08:17.793 []
Lewis     00:10:10.002  00:00:09.182[]
Sten      00:09:04.019  00:00:44.041[1]
Karl      00:09:38.634  00:01:18.656[3]
David     00:10:41.443  00:02:21.465[4, 5, 6]

Igal võidusõidul tuvastatakse ka kiirema ringi tegija (kolme sektori summa). Teie ülesandeks on tuvastada
kes on kiirema ringi teinud. Aega näita isiku järgi peale "koperdatud ringe".

Valtteri 00:12:23.430 [] 00:01:10.037
Lewis    00:14:51.852 00:02:28.422 [3]

Kiirema ringi teinud söitja ei pruugi olla köikides sektorites
kiirem. Ta ei pruugi üheski sektoris kiireim olla. Tuvastage
vöistluse kolme sektrori kiiremad ajad ja soitjad. Lisaks arvutage
lopus kokku klirema ringi aeg sektorite baasil ehk "unistuste ring"
Valtteri 00:12:24.200 [] 00:01:10.814
Lewis 00:16:12.296 00:03:48.096 [3, 10]

Sectors best
Sector 1 Nico       00:00:23.037
Sector 2 Lewis      00:00:23.007
Sector 3 Marko      00:00:23.068
Dream lap time: 00:01:09.112

Kogu võistluse info tuleb kirjutada txt (see on csv sisuga) faili.
Fail sisaldab allolevat infot ja fail peab sisaldama päist.
Ajad on sekundites. Failinimi on Result.txt

Ring;Nimi;Aeg:Sektor1;Sektor2;Sektor3;Viga
1;Lewis;72.778;23.746;24.639;24.393;Jah
2;Nico;72.778;23.746;24.639;24.393;Ei
"""

import random
import csv

racers = ["Karla", "Evelin", "Liise", "Kreete", "Sten"]
alg, lopp = 23, 26
times = []


def suvalineaeg(a, b):
    aeg = round(random.uniform(a, b), 3)
    return aeg


def taisringi_aeg():
    total = 0
    messed_up_laps = []
    for lap in range(1, 11):
        s1 = suvalineaeg(alg, lopp)
        s2 = suvalineaeg(alg, lopp)
        s3 = suvalineaeg(alg, lopp)

        number = random.randint(1, 10)
        if number == 2:
            s1 = suvalineaeg(30, 90)
            s2 = suvalineaeg(30, 90)
            s3 = suvalineaeg(30, 90)
            messed_up_laps.append(lap)

        kokku = round(s1 + s2 + s3, 3)
        total += kokku

    return total, messed_up_laps


for racer in racers:
    total_time, messed_up_laps = taisringi_aeg()
    times.append([racer, total_time, messed_up_laps])

sorted_times = sorted(times, key=lambda x: x[1])


def format_time(total_time):
    hours, minutes = divmod(int(float(total_time)) // 60, 60)
    seconds = int(float(total_time)) % 60
    milliseconds = int(total_time.split(".")[1][:3])
    return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}"


fastest_lap_time = float('inf')
fastest_lap_racer = ""
fastest_lap_messed_up_laps = []

for racer, total_time, messed_up_laps in times:
    if min(messed_up_laps, default=0) == 0:
        if total_time < fastest_lap_time:
            fastest_lap_time = total_time
            fastest_lap_racer = racer
            fastest_lap_messed_up_laps = messed_up_laps

top_racers = []
for i, (racer, time, koperdused) in enumerate(sorted_times[::-1], start=1):
    if racer != fastest_lap_racer:
        top_racers.append((racer, time, koperdused))
    if len(top_racers) == 5:
        break

if len(top_racers) < 5:
    missing_racers = 5 - len(top_racers)
    for i in range(missing_racers):
        racer, time, koperdused = sorted_times[::-1][i]
        top_racers.append((racer, time, koperdused))

if fastest_lap_racer:
    fastest_lap_time_formatted = format_time(str(fastest_lap_time))
    fastest_lap_messed_up_laps_formatted = " ".join(map(str, fastest_lap_messed_up_laps))
    print(f"Fastest Lap Racer:")
    print(f"{fastest_lap_racer:10}{fastest_lap_time_formatted} {fastest_lap_messed_up_laps_formatted if fastest_lap_messed_up_laps else ''}")
    print()

print("Top 5 Racers (Reversed Order):")
for i, (racer, time, koperdused) in enumerate(top_racers, start=1):
    total_time = str(time)
    time_formatted = format_time(total_time)
    koperdused_formatted = " ".join(map(str, koperdused))
    difference = time - sorted_times[0][1]
    difference_formatted = format_time(str(difference))
    if i == 1:
        print(f"Rank   Racer     Time       Difference  Mistakes")
        print(f"{i:<6}{racer:10}{time_formatted} {difference_formatted} {koperdused_formatted if koperdused else ''}")
    else:
        print(f"{i:<6}{racer:10}{time_formatted} {difference_formatted} {koperdused_formatted if koperdused else ''}")

sectors = {
    "Sector 1": [],
    "Sector 2": [],
    "Sector 3": []
}

for racer, total_time, messed_up_laps in times:
    if min(messed_up_laps, default=0) == 0:
        sector_1 = suvalineaeg(23, 26)
        sector_2 = suvalineaeg(23, 26)
        sector_3 = suvalineaeg(23, 26)
        sectors["Sector 1"].append((racer, sector_1))
        sectors["Sector 2"].append((racer, sector_2))
        sectors["Sector 3"].append((racer, sector_3))

print("\nSectors best:")
for sector, results in sectors.items():
    if results:
        best_racer = min(results, key=lambda x: x[1])[0]
        best_time = min(results, key=lambda x: x[1])[1]
        best_time_formatted = format_time(str(best_time))
        print(f"{sector:10}{best_racer:10}{best_time_formatted}")
    else:
        print(f"{sector:10}No valid results")

dream_lap_time = format_time(str(fastest_lap_time + sum(suvalineaeg(23, 26) for _ in range(3))))
print(f"\nDream lap time: {dream_lap_time}")

with open("Result.txt", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Ring", "Nimi", "Aeg:Sektor1", "Sektor2", "Sektor3", "Viga"])
    for i, (racer, total_time, koperdused) in enumerate(times, start=1):
        has_mistakes = bool(koperdused)
        writer.writerow([i, racer, total_time] + [suvalineaeg(23, 26) for _ in range(3)] + [has_mistakes])