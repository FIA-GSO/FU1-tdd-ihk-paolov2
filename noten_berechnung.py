
def berechne_prozent(erreichte_punkte: int, moegliche_punkte: int) -> int:
  if not isinstance(erreichte_punkte, int):
    raise TypeError("Erreichte Punkte ist kein integer wert!")
  if not isinstance(moegliche_punkte, int):
    raise TypeError("Mögliche Punkte ist kein integer wert!")
  
  if erreichte_punkte < 0 or moegliche_punkte < 0:
    raise ValueError("Grenzen dürfen nicht negativ sein!")
  if erreichte_punkte > moegliche_punkte:
    raise ValueError("Erreichte Punkte kann nicht größer als mögliche Punkte sein!")

  prozent = float(erreichte_punkte) / moegliche_punkte
  return int(prozent * 100)

def extrahiere_note(prozent: int) -> str:
  if not isinstance(prozent, int):
    raise TypeError("Prozent muss ein integer sein!")

  if prozent <= 100 and prozent >= 92:
    return "sehr gut"
  elif prozent <= 91 and prozent >= 81:
    return "gut"
  elif prozent <= 80 and prozent >= 67:
    return "befriedigend"
  elif prozent <= 66 and prozent >= 50:
    return "ausreichend"
  elif prozent <= 49 and prozent >= 30:
    return "mangelhaft"
  elif prozent <= 29 and prozent >= 0:
    return "ungenügend"
  
  raise ValueError("Prozent muss zwischen 0 und 100 sein!")
