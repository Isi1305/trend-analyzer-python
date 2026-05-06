#Analyse der Werte
werte = [12, 15, 20, 22, 18, 17]
print(max(werte))
print(min(werte))

average = sum(werte) / len(werte)
print(average)

for wert in werte: #Die Schleife iteriert über jedes Element in der Liste "werte"
    if wert > average: #Vergleicht den aktuellen Wert mit dem Durschnitt
        print(f"{wert} ist über dem Durschnitt.")
    elif wert < average:
        print(f"{wert} ist unter dem Durschnitt.")
    elif wert == average:
        print(f"{wert} ist gleich dem Durschnitt.")

#Bestimmung des Trends
if werte[-1] > werte[0]: 
    print("Trend steigend")
elif werte[-1] < werte[0]:
    print("Trend fallend")
else:
    print("Trend stabil")

def determine_trend(werte):
    for i in range(len(werte) - 1): #Die Schleife läuft von 0 bis zur vorletzten Position.
        if werte[i +1] > werte[i]: #Vergleich der Werte, um den Trend zu bestimmen #Für mich: i + 1 = „Geh eine Position weiter nach rechts in der Liste“
            print(f"Von {werte[i] } zu {werte[i + 1]}: steigend")
        elif werte [i + 1] < werte[i]:
            print(f"Von {werte[i]} zu {werte[i + 1]}: fallend")
        elif werte[i + 1] == werte[i]:
            print(f"Von {werte[i]} zu {werte[i + 1]}: stabil")


def calculate_trend_score(werte):
    score = 0 #Variable, die den Trend bewertet. Sie wird um 1 erhöht, wenn der Trend strigt und verringert, wenn er fällt.
    for i in range(len(werte) - 1):
        if werte[i +1] > werte[i]:
            score += 1
        elif werte [i + 1] < werte[i]:
            score -= 1
        elif werte[i + 1] == werte[i]: #Unnötig, da der Score sich nit verändert, aber gut als Übung.
            score += 0
    return score

score = calculate_trend_score(werte)
print(f"Trend Score: {score}")

if score > 0:
    print("Der allgemeine Trend ist steigend.")
elif score < 0:
    print("Der allgemeine Trend ist fallend.")
elif score == 0:
    print("Der allgemeine Trend ist stabil.")


#Visualisierung der Werte
import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.plot(werte, marker='o', color='orange')
plt.title('Werte über die Zeit')
plt.xlabel('Zeit')
plt.ylabel('Werte')
plt.grid(True, alpha=0.3)
plt.show()