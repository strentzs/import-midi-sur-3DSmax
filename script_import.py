import mido
from pymxs import runtime as rt

# Chemin vers le fichier MIDI
midi_file_path = "midi_export.mid"

# Ouvrir le fichier MIDI
midi_file = mido.MidiFile(midi_file_path)

# Liste pour stocker les informations de note
notes_data = []

# Parcourir les pistes MIDI
for track in midi_file.tracks:
    # Parcourir les messages MIDI dans chaque piste
    time_counter = 0
    for message in track:
        # Vérifier le type de message
        if message.type == 'note_on':
            # Extraire les informations de note
            note_number = message.note
            velocity = message.velocity
            duration = 0

            # Rechercher le message "note_off" correspondant
            for next_message in track[track.index(message) + 1:]:
                if next_message.type == 'note_off' and next_message.note == note_number:
                    duration = next_message.time
                    break

            # Ajouter les informations de note à la liste
            notes_data.append((note_number, velocity, time_counter, duration))

        # Mettre à jour le compteur de temps
        time_counter += message.time

# Chemin vers le fichier de sortie
output_file_path = "notes_output.txt"

# Écrire les informations de note dans le fichier de sortie
with open(output_file_path, 'w') as output_file:
    for note_data in notes_data:
        output_file.write(f"Note: {note_data[0]}, Vélocité: {note_data[1]}, Timestamp: {note_data[2]}, Durée: {note_data[3]}\n")

# Afficher un message de confirmation
print(f"Les informations de note ont été enregistrées dans le fichier {output_file_path}.")

# Associer les numéros de note aux noms des objets 3DS Max
note_mapping = {
    0: "box_000",
    1: "box_001",
    2: "box_002",
    3: "box_003",
    4: "box_004",
    5: "box_005",
    6: "box_006",
    7: "box_007",
    8: "box_008",
    9: "box_009",
    10: "box_010",
    11: "box_011",
    12: "box_012",
    13: "box_013",
    14: "box_014",
    15: "box_015",
    16: "box_016",
    17: "box_017",
    18: "box_018",
    19: "box_019",
    20: "box_020",
    21: "box_021",
    22: "box_022",
    23: "box_023",
    24: "box_024",
    25: "box_025",
    26: "box_026",
    27: "box_027",
    28: "box_028",
    29: "box_029",
    30: "box_030",
    31: "box_031",
    32: "box_032",
    33: "box_033",
    34: "box_034",
    35: "box_035",
    36: "box_036",
    37: "box_037",
    38: "box_038",
    39: "box_039",
    40: "box_040",
    41: "box_041",
    42: "box_042",
    43: "box_043",
    44: "box_044",
    45: "box_045",
    46: "box_046",
    47: "box_047",
    48: "box_048",
    49: "box_049",
    50: "box_050",
    51: "box_051",
    52: "box_052",
    53: "box_053",
    54: "box_054",
    55: "box_055",
    56: "box_056",
    57: "box_057",
    58: "box_058",
    59: "box_059",
    60: "box_060",
    61: "box_061",
    62: "box_062",
    63: "box_063",
    64: "box_064",
    65: "box_065",
    66: "box_066",
    67: "box_067",
    68: "box_068",
    69: "box_069",
    70: "box_070",
    71: "box_071",
    72: "box_072",
    73: "box_073",
    74: "box_074",
    75: "box_075",
    76: "box_076",
    77: "box_077",
    78: "box_078",
    79: "box_079",
    80: "box_080",
    81: "box_081",
    82: "box_082",
    83: "box_083",
    84: "box_084",
    85: "box_085",
    86: "box_086",
    87: "box_087",
    88: "box_088",
}

# Parcourir les informations de note
for note_data in notes_data:
    note_number = note_data[0]
    velocity = note_data[1]
    time_counter = note_data[2]
    duration = note_data[3]

    # Vérifier si la note est présente dans le mapping
    if note_number in note_mapping:
        # Récupérer le nom de l'objet 3DS Max associé
        object_name = note_mapping[note_number]

        # Rechercher l'objet dans la scène 3DS Max
        note_object = rt.getNodeByName(object_name)

        # Vérifier si l'objet a été trouvé
        if note_object is not None:
            # Appliquer les transformations à l'objet
            rt.currentTime = time_counter
            note_object.pos.z -= 2.98  # Valeur X de la translation sur l'axe Z
            rt.animate(note_object.controller, rt.controller().percentKeys, rt.PositionXYZ.controller)
            rt.currentTime = time_counter + duration
            note_object.pos.z += 2.98  # Valeur X de la translation sur l'axe Z
            rt.animate(note_object.controller, rt.controller().percentKeys, rt.PositionXYZ.controller)
        else:
            print("Objet non trouvé pour la note:", note_number)
    else:
        print("Note non associée dans le mapping:", note_number)
