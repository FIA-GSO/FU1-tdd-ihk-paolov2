import pytest

from noten_berechnung import berechne_prozent, extrahiere_note

# region Positivtests berechne_prozent

def test_berechne_prozent__normalfall():
  # Arrange
  moegliche_punkte: int = 86
  erreichte_punkte: int = 15
  soll_ergebnis: int = 17

  # Act
  ist_ergebnis: int = berechne_prozent(erreichte_punkte, moegliche_punkte)

  # Assert
  assert ist_ergebnis == soll_ergebnis

# endregion Positivtests berechne_prozent

# region Positivtests extrahiere_note

def test_extrahiere_note__sehr_gut_minimum():
  # Arrange
  erreichte_prozent: int = 92
  soll_ergebnis: str = "sehr gut"

  # Act
  ist_ergebnis: str = extrahiere_note(erreichte_prozent)

  # Assert
  assert ist_ergebnis == soll_ergebnis

def test_extrahiere_note__sehr_gut_maximum():
  # Arrange
  erreichte_prozent: int = 100
  soll_ergebnis: str = "sehr gut"

  # Act
  ist_ergebnis: str = extrahiere_note(erreichte_prozent)

  # Assert
  assert ist_ergebnis == soll_ergebnis

def test_extrahiere_note__gut_minimum():
  # Arrange
  erreichte_prozent: int = 81
  soll_ergebnis: str = "gut"

  # Act
  ist_ergebnis: str = extrahiere_note(erreichte_prozent)

  # Assert
  assert ist_ergebnis == soll_ergebnis

def test_extrahiere_note__gut_maximum():
  # Arrange
  erreichte_prozent: int = 91
  soll_ergebnis: str = "gut"

  # Act
  ist_ergebnis: str = extrahiere_note(erreichte_prozent)

  # Assert
  assert ist_ergebnis == soll_ergebnis

def test_extrahiere_note__befriedigend_minimum():
  # Arrange
  erreichte_prozent: int = 67
  soll_ergebnis: str = "befriedigend"

  # Act
  ist_ergebnis: str = extrahiere_note(erreichte_prozent)

  # Assert
  assert ist_ergebnis == soll_ergebnis

def test_extrahiere_note__befriedigend_maximum():
  # Arrange
  erreichte_prozent: int = 80
  soll_ergebnis: str = "befriedigend"

  # Act
  ist_ergebnis: str = extrahiere_note(erreichte_prozent)

  # Assert
  assert ist_ergebnis == soll_ergebnis

def test_extrahiere_note__ausreichend_minimum():
  # Arrange
  erreichte_prozent: int = 50
  soll_ergebnis: str = "ausreichend"

  # Act
  ist_ergebnis: str = extrahiere_note(erreichte_prozent)

  # Assert
  assert ist_ergebnis == soll_ergebnis

def test_extrahiere_note__ausreichend_maximum():
  # Arrange
  erreichte_prozent: int = 66
  soll_ergebnis: str = "ausreichend"

  # Act
  ist_ergebnis: str = extrahiere_note(erreichte_prozent)

  # Assert
  assert ist_ergebnis == soll_ergebnis

def test_extrahiere_note__mangelhaft_minimum():
  # Arrange
  erreichte_prozent: int = 30
  soll_ergebnis: str = "mangelhaft"

  # Act
  ist_ergebnis: str = extrahiere_note(erreichte_prozent)

  # Assert
  assert ist_ergebnis == soll_ergebnis

def test_extrahiere_note__mangelhaft_maximum():
  # Arrange
  erreichte_prozent: int = 49
  soll_ergebnis: str = "mangelhaft"

  # Act
  ist_ergebnis: str = extrahiere_note(erreichte_prozent)

  # Assert
  assert ist_ergebnis == soll_ergebnis

def test_extrahiere_note__ungenuegend_minimum():
  # Arrange
  erreichte_prozent: int = 0
  soll_ergebnis: str = "ungenügend"

  # Act
  ist_ergebnis: str = extrahiere_note(erreichte_prozent)

  # Assert
  assert ist_ergebnis == soll_ergebnis

def test_extrahiere_note__ungenuegend_maximum():
  # Arrange
  erreichte_prozent: int = 29
  soll_ergebnis: str = "ungenügend"

  # Act
  ist_ergebnis: str = extrahiere_note(erreichte_prozent)

  # Assert
  assert ist_ergebnis == soll_ergebnis

# endregion Positivtests

# region Negativtests berechne_prozent

def test_berechne_prozent__erreichte_punkte_groesser_als_moegliche_punkte():
  # Arrange
  moegliche_punkte: int = 100
  erreichte_punkte: int = 101

  # Act & Assert
  with pytest.raises(ValueError):
    berechne_prozent(erreichte_punkte, moegliche_punkte)

def test_berechne_prozent__erreichte_punkte_ist_negativ():
  # Arrange
  moegliche_punkte: int = 100
  erreichte_punkte: int = -1

  # Act & Assert
  with pytest.raises(ValueError):
    berechne_prozent(erreichte_punkte, moegliche_punkte)

def test_berechne_prozent__moegliche_punkte_ist_negativ():
  # Arrange
  moegliche_punkte: int = -1
  erreichte_punkte: int = 100

  # Act & Assert
  with pytest.raises(ValueError):
    berechne_prozent(erreichte_punkte, moegliche_punkte)
    
def test_berechne_prozent__erreichte_punkte_und_moegliche_punkte_sind_negativ():
  # Arrange
  moegliche_punkte: int = -1
  erreichte_punkte: int = -10

  # Act & Assert
  with pytest.raises(ValueError):
    berechne_prozent(erreichte_punkte, moegliche_punkte)

def test_berechne_prozent__erreichte_punkte_kein_int():
  # Arrange
  moegliche_punkte: int = 100
  erreichte_punkte: str = "10"

  # Act & Assert
  with pytest.raises(TypeError):
    berechne_prozent(erreichte_punkte, moegliche_punkte)

def test_berechne_prozent__moegliche_punkte_kein_int():
  # Arrange
  moegliche_punkte: str = "100"
  erreichte_punkte: int = 10

  # Act & Assert
  with pytest.raises(TypeError):
    berechne_prozent(erreichte_punkte, moegliche_punkte)

# endregion Negativtests berechne_prozent

# region Negativtests extrahiere_note

def test_extrahiere_note__negativ_prozent():
  # Arrange
  prozent: int = -10

  # Act & Assert
  with pytest.raises(ValueError):
    extrahiere_note(prozent)

def test_extrahiere_note__prozent_ueber_hundert():
  # Arrange
  prozent: int = 101

  # Act & Assert
  with pytest.raises(ValueError):
    extrahiere_note(prozent)

def test_extrahiere_note__prozent_kein_int():
  # Arrange
  prozent: str = "100"

  # Act & Assert
  with pytest.raises(TypeError):
    extrahiere_note(prozent)

# endregion Negativtests extrahiere_note
