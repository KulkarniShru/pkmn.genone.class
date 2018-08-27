#PokemonClassifierGenOne

#*HOW TO INSTALL*
#Choose the appropriate installer for your hardware and install Python 3.7.0. Now that you have done that, download this program.
#Open terminal/command prompt and simply copy-paste the location into terminal/command prompt. Once this is done, press enter/return and the program should be fully functional.

#*HOW TO USE*
#Once the program is open, you will be greeted with a question, "Which Pokemon would you like to learn about?". You can type in the name of any GENERATION ONE (Kanto) Pokemon and you will be given it's name, what kind of Pokemon it is (for example, Pikachu is the mouse Pokemon), its National Pokedex number, and it's typing.
#If you would like to exit the program, you can type quit, quit(), end, or stop. This will terminate the loop that runs the question and thus close the program.

#This part defines the  class
class Pokemon:
	name = ""
	kind = ""
	number = -1
	typing = ""
	def desc(self): 
		description = "%s, the %s Pokemon, is a %s type. It is number %s in the National Pokedex." % (self.name, self.kind, self.typing, self.number)
		return description

# A Pokemon Classifications
Abra = Pokemon()
Abra.name, Abra.kind, Abra.number, Abra.typing = "Abra", "Psi", 63, "Psychic"

Aerodactyl = Pokemon()
Aerodactyl.name, Aerodactyl.kind, Aerodactyl.number, Aerodactyl.typing = "Aerodactyl", "Fossil", 142, "Rock and Flying"

Alakazam = Pokemon()
Alakazam.name, Alakazam.kind, Alakazam.number, Alakazam.typing = "Alakazam", "Psi", 65, "Psychic"

Arbok = Pokemon()
Arbok.name, Arbok.kind, Arbok.number, Arbok.typing = "Arbok", "Cobra", 24, "Poison"

Arcanine = Pokemon()
Arcanine.name, Arcanine.kind, Arcanine.number, Arcanine.typing = "Arcanine", "Legendary", 59, "Fire"

Articuno = Pokemon()
Articuno.name, Articuno.kind, Articuno.number, Articuno.typing = "Articuno", "Freeze", 144, "Ice and Flying"

#B Pokemon Classifications
Beedrill = Pokemon()
Beedrill.name, Beedrill.kind, Beedrill.number, Beedrill.typing = "Beedrill", "Poison Bee", 15, "Bug and Poison"

Bellsprout = Pokemon()
Bellsprout.name, Bellsprout.kind, Bellsprout.number, Bellsprout.typing = "Bellsprout", "Flower", 69, "Grass and Poison"

Blastoise = Pokemon()
Blastoise.name, Blastoise.kind, Blastoise.number, Blastoise.typing = "Blastoise", "Shellfish", 9, "Water"

Bulbasaur = Pokemon()
Bulbasaur.name, Bulbasaur.kind, Bulbasaur.number, Bulbasaur.typing = "Bulbasaur", "Seed", 1, "Grass and Poison"

Butterfree = Pokemon()
Butterfree.name, Butterfree.kind, Butterfree.number, Butterfree.typing = "Butterfree", "Butterfly", 12, "Bug and Flying"

#C Pokemon Classifications
Caterpie = Pokemon()
Caterpie.name, Caterpie.kind, Caterpie.number, Caterpie.typing = "Caterpie", "Worm", 10, "Bug"

Chansey = Pokemon()
Chansey.name, Chansey.kind, Chansey.number, Chansey.name = "Chansey", "Egg", 113, "Normal"

Charizard = Pokemon()
Charizard.name, Charizard.kind, Charizard.number, Charizard.typing = "Charizard", "Flame", 6, "Fire and Flying"

Charmander =  Pokemon()
Charmander.name, Charmander.kind, Charmander.number, Charmander.typing = "Charmander", "Lizard", 4, "Fire"

Charmeleon = Pokemon()
Charmeleon.name, Charmeleon.kind, Charmeleon.number, Charmeleon.typing = "Charmeleon", "Flame", 5, "Fire"

Clefable = Pokemon()
Clefable.name, Clefable.kind, Clefable.number, Clefable.typing = "Clefable", "Fairy", 36, "Fairy"

Clefairy = Pokemon()
Clefairy.name, Clefairy.kind, Clefairy.number, Clefairy.typing = "Clefairy", "Fairy", 35, "Fairy"

Cloyster = Pokemon()
Cloyster.name, Cloyster.kind, Cloyster.number, Cloyster.typing = "Cloyster", "Bivalve", 91, "Water and Ice"

Cubone = Pokemon()
Cubone.name, Cubone.kind, Cubone.number, Cubone.typing = "Cubone", "Lonely", 104, "Ground"

#D Pokemon Classifications
Dewgong = Pokemon()
Dewgong.name, Dewgong.kind, Dewgong.number, Dewgong.typing = "Dewgong", "Sea Lion", 87, "Water and Ice"

Diglett = Pokemon()
Diglett.name, Diglett.kind, Diglett.number, Diglett.typing = "Diglett", "Mole", 50, "Ground"

Ditto = Pokemon()
Ditto.name, Ditto.kind, Ditto.number, Ditto.typing = "Ditto", "Transform", 132, "Normal"

Dodrio = Pokemon()
Dodrio.name, Dodrio.kind, Dodrio.number, Dodrio.typing = "Dodrio", "Triple Bird", 85, "Normal and Flying"

Doduo = Pokemon()
Doduo.name, Doduo.kind, Doduo.number, Doduo.typing = "Doduo", "Twin Bird", 84, "Normal and Flying"

Dragonair = Pokemon()
Dragonair.name, Dragonair.kind, Dragonair.number, Dragonair.typing = "Dragonair", "Dragon", 148, "Dragon"

Dragonite = Pokemon()
Dragonite.name, Dragonite.kind, Dragonite.number, Dragonite.typing = "Dragonite", "Dragon", 149, "Dragon and Flying"

Dratini = Pokemon()
Dratini.name, Dratini.kind, Dratini.number, Dratini.typing = "Dratini", "Dragon", 147, "Dragon"

Drowzee = Pokemon()
Drowzee.name, Drowzee.kind, Drowzee.number, Drowzee.typing = "Drowzee", "Hypnosis", 96, "Psychic"

Dugtrio = Pokemon()
Dugtrio.name, Dugtrio.kind, Dugtrio.number, Dugtrio.typing = "Dugtrio", "Mole", 51, "Ground"

#E Pokemon Classifications
Eevee = Pokemon()
Eevee.name, Eevee.kind, Eevee.number, Eevee.typing = "Eevee", "Evolution", 133, "Normal"

Ekans = Pokemon()
Ekans.name, Ekans.kind, Ekans.number, Ekans.typing = "Ekans", "Snake", 23, "Poison"

Electabuzz = Pokemon()
Electabuzz.name, Electabuzz.kind, Electabuzz.number, Electabuzz.typing = "Electabuzz", "Electric", 125, "Electric"

Electrode = Pokemon()
Electrode.name, Electrode.kind, Electrode.number, Electrode.typing = "Electrode", "Ball", 101, "Electric"

Exeggcute = Pokemon()
Exeggcute.name, Exeggcute.kind, Exeggcute.number, Exeggcute.typing = "Exeggcute", "Egg", 102, "Grass and Psychic"

Exeggutor = Pokemon()
Exeggutor.name, Exeggutor.kind, Exeggutor.number, Exeggutor.typing = "Exeggutor", "Coconut", 103, "Grass and Psychic"

#F Pokemon Classifications
Farfetchd = Pokemon()
Farfetchd.name, Farfetchd.kind, Farfetchd.number, Farfetchd.typing = "Farfetchd", "Wild Duck", 83, "Normal and Flying"

Fearow = Pokemon()
Fearow.name, Fearow.kind, Fearow.number, Fearow.typing = "Fearow", "Beak", 22, "Normal and Flying"

Flareon = Pokemon()
Flareon.name, Flareon.kind, Flareon.number, Flareon.typing = "Flareon", "Flame", 136, "Fire"

#G Pokemon Classifications
Gastly = Pokemon()
Gastly.name, Gastly.kind, Gastly.number, Gastly.typing = "Gastly", "Gas", 92, "Ghost and Poison"

Gengar = Pokemon()
Gengar.name, Gengar.kind, Gengar.number, Gengar.typing = "Gengar", "Shadow", 94, "Ghost and Poison"

Geodude = Pokemon()
Geodude.name, Geodude.kind, Geodude.number, Geodude.typing = "Geodude", "Rock", 74, "Rock and Ground"

Gloom = Pokemon()
Gloom.name, Gloom.kind, Gloom.number, Gloom.typing = "Gloom", "Weed", 44, "Grass and Poison"

Golbat = Pokemon()
Golbat.name, Golbat.kind, Golbat.number, Golbat.typing = "Golbat", "Bat", 42, "Poison and Flying"

Goldeen = Pokemon()
Goldeen.name, Goldeen.kind, Goldeen.number, Goldeen.typing = "Goldeen", "Goldfish", 118, "Water"

Golduck = Pokemon()
Golduck.name, Golduck.kind, Golduck.number, Goldeen.typing = "Golduck", "Duck", 55, "Water"

Golem = Pokemon()
Golem.name, Golem.kind, Golem.number, Golem.typing = "Golem", "Megaton", 76, "Rock and Ground"

Graveler = Pokemon()
Graveler.name, Graveler.kind, Graveler.number, Graveler.typing = "Graveler", "Rock", 75, "Rock and Ground"

Grimer = Pokemon()
Grimer.name, Grimer.kind, Grimer.number, Grimer.typing = "Grimer", "Sludge", 88, "Poison"

Growlithe = Pokemon()
Growlithe.name, Growlithe.kind, Growlithe.number, Growlithe.typing = "Growlithe", "Puppy", 58, "Fire"

Gyarados = Pokemon()
Gyarados.name, Gyarados.kind, Gyarados.number, Gyarados.typing = "Gyarados", "Atrocious", 130, "Water and Flying"

#H Pokemon Classifications
Haunter = Pokemon()
Haunter.name, Haunter.kind, Haunter.number, Haunter.typing = "Haunter", "Gas", 93, "Ghost and Poison"

Hitmonchan = Pokemon()
Hitmonchan.name, Hitmonchan.kind, Hitmonchan.number, Hitmonchan.typing = "Hitmonchan", "Punching", 107, "Fighting"

Hitmonlee = Pokemon()
Hitmonlee.name, Hitmonlee.kind, Hitmonlee.number, Hitmonlee.typing = "Hitmonlee", "Kicking", 106, "Fighting"

Horsea = Pokemon()
Horsea.name, Horsea.kind, Horsea.number, Horsea.typing = "Horsea", "Dragon", 116, "Water"

Hypno = Pokemon()
Hypno.name, Hypno.kind, Hypno.number, Hypno.typing = "Hypno", "Hypnosis", 97, "Psychic"

#I Pokemon Classifications
Ivysaur = Pokemon()
Ivysaur.name, Ivysaur.kind, Ivysaur.number, Ivysaur.typing = "Ivysaur", "Seed", 2, "Grass and Poison"

#J Pokemon Classifications
Jigglypuff = Pokemon()
Jigglypuff.name, Jigglypuff.kind, Jigglypuff.number, Jigglypuff.typing = "Jigglypuff", "Balloon", 39, "Normal and Fairy"

Jolteon = Pokemon()
Jolteon.name, Jolteon.kind, Jolteon.number, Jolteon.typing = "Jolteon", "Lightning", 135, "Electric"

Jynx = Pokemon()
Jynx.name, Jynx.kind, Jynx.number, Jynx.typing = "Jynx", "Human Shape", 124, "Ice and Psychic"

#K Pokemon Classifications
Kabuto = Pokemon()
Kabuto.name, Kabuto.kind, Kabuto.number, Kabuto.typing = "Kabuto", "Shellfish", 140, "Rock and Water"

Kabutops = Pokemon()
Kabutops.name, Kabutops.kind, Kabutops.number, Kabutops.typing = "Kabutops", "Shellfish", 141, "Rock and Water"

Kadabra = Pokemon()
Kadabra.name, Kadabra.kind, Kadabra.number, Kadabra.typing = "Kadabra", "Psi", 64, "Psychic"

Kakuna = Pokemon()
Kakuna.name, Kakuna.kind, Kakuna.number, Kakuna.typing = "Kakuna", "Cocoon", 14, "Bug and Poison"

Kangaskhan = Pokemon()
Kangaskhan.name, Kangaskhan.kind, Kangaskhan.number, Kangaskhan.typing = "Kangaskhan", "Parent", 115, "Normal"

Kingler = Pokemon()
Kingler.name, Kingler.kind, Kingler.number, Kingler.typing = "Kingler", "Pincer", 99, "Water"

Koffing = Pokemon()
Koffing.name, Koffing.kind, Koffing.number, Koffing.typing = "Koffing", "Poison Gas", 109, "Poison"

Krabby = Pokemon()
Krabby.name, Krabby.kind, Krabby.number, Krabby.typing = "Krabby", "River Crab", 98, "Water"

#L Pokemon Classifications
Lapras = Pokemon()
Lapras.name, Lapras.kind, Lapras.number, Lapras.typing = "Lapras", "Transport", 131, "Water and Ice"

Lickitung = Pokemon()
Lickitung.name, Lickitung.kind, Lickitung.number, Lickitung.typing = "Lickitung", "Licking", 108, "Normal"

#M Pokemon Classifications
Machamp = Pokemon()
Machamp.name, Machamp.kind, Machamp.number, Machamp.typing = "Machamp", "Superpower", 68, "Fighting"

Machoke = Pokemon()
Machoke.name, Machoke.kind, Machoke.number, Machoke.typing = "Machoke", "Superpower", 67, "Fighting"

Machop = Pokemon()
Machop.name, Machop.kind, Machop.number, Machop.typing = "Machop", "Superpower", 66, "Fighting"

Magikarp = Pokemon()
Magikarp.name, Magikarp.kind, Magikarp.number, Magikarp.typing = "Magikarp", "Fish", 129, "Water"

Magmar = Pokemon()
Magmar.name, Magmar.kind, Magmar.number, Magmar.typing = "Magmar", "Spitfire", 126, "Fire"

Magnemite = Pokemon()
Magnemite.name, Magnemite.kind, Magnemite.number, Magnemite.typing = "Magnemite", "Magnet", 81, "Electric and Steel"

Magneton = Pokemon()
Magneton.name, Magneton.kind, Magneton.number, Magneton.typing = "Magneton", "Magnet", 82, "Electric and Steel"

Mankey = Pokemon()
Mankey.name, Mankey.kind, Mankey.number, Mankey.typing = "Mankey", "Pig Monkey", 56, "Fighting"

Marowak = Pokemon()
Marowak.name, Marowak.kind, Marowak.number, Marowak.typing = "Marowak", "Bone Keeper", 105, "Ground"

Meowth = Pokemon()
Meowth.name, Meowth.kind, Meowth.number, Meowth.typing = "Meowth", "Scratch Cat", 52, "Normal"

Metapod = Pokemon()
Metapod.name, Metapod.kind, Metapod.number, Metapod.typing = "Metapod", "Cocoon", 11, "Bug"

Mew = Pokemon()
Mew.name, Mew.kind, Mew.number, Mew.typing = "Mew", "New Species", 151, "Psychic"

Mewtwo = Pokemon()
Mewtwo.name, Mewtwo.kind, Mewtwo.number, Mewtwo.typing = "Mewtwo", "Genetic", 150, "Psychic"

Moltres = Pokemon()
Moltres.name, Moltres.kind, Moltres.number, Moltres.typing = "Moltres", "Flame", 146, "Fire and Flying"

MrMime = Pokemon()
MrMime.name, MrMime.kind, MrMime.number, MrMime.typing = "Mr. Mime", "Barrier", 122, "Psychic and Fairy"

Muk = Pokemon()
Muk.name, Muk.kind, Muk.number, Muk.typing = "Muk", "Sludge", 89, "Poison"

#N Pokemon Classifications
Nidoking = Pokemon()
Nidoking.name, Nidoking.kind, Nidoking.number, Nidoking.typing = "Nidoking", "Drill", 34, "Poison and Ground"

Nidoqueen = Pokemon()
Nidoqueen.name, Nidoqueen.kind, Nidoqueen.number, Nidoqueen.typing = "Nidoqueen", "Drill", 31, "Poison and Ground"

Nidoran = Pokemon()
Nidoran.name, Nidoran.kind, Nidoran.number, Nidoran.typing = "Nidoran", "Poison Pin", "29 (F) or 31 (M)", "Poison"

Nidorina = Pokemon()
Nidorina.name, Nidorina.kind, Nidorina.number, Nidorina.typing = "Nidorina", "Poison Pin", 30, "Poison"

Nidorino = Pokemon()
Nidorino.name, Nidorino.kind, Nidorino.number, Nidorino.typing = "Nidorino", "Poison Pin", 33, "Poison"

Ninetales = Pokemon()
Ninetales.name, Ninetales.kind, Ninetales.number, Ninetales.typing = "Ninetales", "Fox", 38, "Fire"

#O Pokemon Classifications
Oddish = Pokemon()
Oddish.name, Oddish.kind, Oddish.number, Oddish.typing = "Oddish", "Weed", 43, "Grass and Poison"

Omanyte = Pokemon()
Omanyte.name, Omanyte.kind, Omanyte.number, Omanyte.typing = "Omanyte", "Spiral", 138, "Rock and Water"

Omastar = Pokemon()
Omastar.name, Omastar.kind, Omastar.number, Omastar.typing = "Omastar", "Spiral", 139, "Rock and Water"

Onix = Pokemon()
Onix.name, Onix.kind, Onix.number, Onix.typing = "Onix", "Rock Snake", 95, "Rock and Ground"

#P Pokemon Classifications
Paras = Pokemon()
Paras.name, Paras.kind, Paras.number, Paras.typing = "Paras", "Mushroom", 46, "Bug and Grass"

Parasect = Pokemon()
Parasect.name, Parasect.kind, Parasect.number, Parasect.typing = "Parasect", "Mushroom", 47, "Bug and Grass"

Persian = Pokemon()
Persian.name, Persian.kind, Persian.number, Persian.typing = "Persian", "Classy Cat", 53, "Normal"

Pidgeot = Pokemon()
Pidgeot.name, Pidgeot.kind, Pidgeot.number, Pidgeot.typing = "Pidgeot", "Bird", 18, "Normal and Flying"

Pidgeotto = Pokemon()
Pidgeotto.name, Pidgeotto.kind, Pidgeotto.number, Pidgeotto.typing = "Pidgeotto", "Bird", 17, "Normal and Flying"

Pidgey = Pokemon()
Pidgey.name, Pidgey.kind, Pidgey.number, Pidgey.typing = "Pidgey", "Bird", 16, "Normal and Flying"

Pikachu = Pokemon()
Pikachu.name, Pikachu.kind, Pikachu.number, Pikachu.typing = "Pikachu", "Mouse", 25, "Electric"

Pinsir = Pokemon()
Pinsir.name, Pinsir.kind, Pinsir.number, Pinsir.typing = "Pinsir", "Stag Beetle", 127, "Bug"

Poliwag = Pokemon()
Poliwag.name, Poliwag.kind, Poliwag.number, Poliwag.typing = "Poliwag", "Tadpole", 60, "Water"

Poliwhirl = Pokemon()
Poliwhirl.name, Poliwhirl.kind, Poliwhirl.number, Poliwhirl.typing = "Poliwhirl", "Tadpole", 61, "Water"

Poliwrath = Pokemon()
Poliwrath.name, Poliwrath.kind, Poliwrath.number, Poliwrath.typing = "Poliwrath", "Tadpole", 62, "Water and Fighting"

Ponyta = Pokemon()
Ponyta.name, Ponyta.kind, Ponyta.number, Ponyta.typing = "Ponyta", "Fire Horse", 77, "Fire"

Porygon = Pokemon()
Porygon.name, Porygon.kind, Porygon.number, Porygon.typing = "Porygon", "Virtual", 137, "Normal"

Primeape = Pokemon()
Primeape.name, Primeape.kind, Primeape.number, Primeape.typing = "Primeape", "Pig Monkey", 57, "Fighting"

Psyduck = Pokemon()
Psyduck.name, Psyduck.kind, Psyduck.number, Psyduck.typing = "Psyduck", "Duck", 54, "Water"

#R Pokemon Classifications
Raichu = Pokemon()
Raichu.name, Raichu.kind, Raichu.number, Raichu.typing = "Raichu", "Mouse", 26, "Electric"

Rapidash = Pokemon()
Rapidash.name, Rapidash.kind, Rapidash.number, Rapidash.typing = "Rapidash", "Fire House", 78, "Fire"

Raticate = Pokemon()
Raticate.name, Raticate.kind, Raticate.number, Raticate.typing = "Raticate", "Mouse", 20, "Normal"

Rattata = Pokemon()
Rattata.name, Rattata.kind, Rattata.number, Rattata.typing = "Rattata", "Mouse", 19, "Normal"

Rhydon = Pokemon()
Rhydon.name, Rhydon.kind, Rhydon.number, Rhydon.typing = "Rhydon", "Drill", 112, "Rock and Ground"

Rhyhorn = Pokemon()
Rhyhorn.name, Rhyhorn.kind, Rhyhorn.number, Rhyhorn.typing = "Rhyhorn", "Spikes", 111, "Rock and Ground"

#S Pokemon Classifications
Sandshrew = Pokemon()
Sandshrew.name, Sandshrew.kind, Sandshrew.number, Sandshrew.typing = "Sandshrew", "Mouse", 27, "Ground"

Sandslash = Pokemon()
Sandslash.name, Sandslash.kind, Sandslash.number, Sandslash.typing = "Sandslash", "Mouse", 28, "Ground"

Scyther = Pokemon()
Scyther.name, Scyther.kind, Scyther.number, Scyther.typing = "Scyther", "Mantis", 123, "Bug and Flying"

Seadra = Pokemon()
Seadra.name, Seadra.kind, Seadra.number, Seadra.typing = "Seadra", "Dragon", 117, "Water"

Seaking = Pokemon()
Seaking.name, Seaking.kind, Seaking.number, Seaking.typing = "Seaking", "Goldfish", 119, "Water"

Seel = Pokemon()
Seel.name, Seel.kind, Seel.number, Seel.typing = "Seel", "Sea Lion", 86, "Water"

Shellder = Pokemon()
Shellder.name, Shellder.kind, Shellder.number, Shellder.typing = "Shellder", "Bivalve", 90, "Water"

Slowbro = Pokemon()
Slowbro.name, Slowbro.kind, Slowbro.number, Slowbro.typing = "Slowbro", "Hermit Crab", 80, "Water and Psychic"

Slowpoke = Pokemon()
Slowpoke.name, Slowpoke.kind, Slowpoke.number, Slowpoke.typing = "Slowpoke", "Dopey", 79, "Water and Psychic"

Snorlax = Pokemon()
Snorlax.name, Snorlax.kind, Snorlax.number, Snorlax.typing = "Snorlax", "Sleeping", 143, "Normal"

Spearow = Pokemon()
Spearow.name, Spearow.kind, Spearow.number, Spearow.typing = "Spearow", "Tiny Bird", 21, "Normal and Flying"

Squirtle = Pokemon()
Squirtle.name, Squirtle.kind, Squirtle.number, Squirtle.typing = "Squirtle", "Tiny Turtle", 7, "Water"

Starmie = Pokemon()
Starmie.name, Starmie.kind, Starmie.number, Starmie.typing = "Starmie", "Mysterious", 121, "Water and Psychic"

Staryu = Pokemon()
Staryu.name, Staryu.kind, Staryu.number, Staryu.typing = "Staryu", "Star Shape", 120, "Water"

#T Pokemon Classifications
Tangela = Pokemon()
Tangela.name, Tangela.kind, Tangela.number, Tangela.typing = "Tangela", "Vine", 114, "Grass"

Tauros = Pokemon()
Tauros.name, Tauros.kind, Tauros.number, Tauros.typing = "Tauros", "Wild Bull", 128, "Normal"

Tentacool = Pokemon()
Tentacool.name, Tentacool.kind, Tentacool.number, Tentacool.typing = "Tentacool", "Jellyfish", 72, "Water and Poison"

Tentacruel = Pokemon()
Tentacruel.name, Tentacruel.kind, Tentacruel.number, Tentacruel.typing = "Tentacruel", "Jellyfish", 73, "Water and Poison"

#V Pokemon Classifications
Vaporeon = Pokemon()
Vaporeon.name, Vaporeon.kind, Vaporeon.number, Vaporeon.typing = "Vaporeon", "Bubble Jet", 134, "Water"

Venomoth = Pokemon()
Venomoth.name, Venomoth.kind, Venomoth.number, Venomoth.typing = "Venomoth", "Poison Moth", 49, "Bug and Poison"

Venonat = Pokemon()
Venonat.name, Venonat.kind, Venonat.number, Venonat.typing = "Venonat", "Insect", 48, "Bug and Poison"

Venusaur = Pokemon()
Venusaur.name, Venusaur.kind, Venusaur.number, Venusaur.typing = "Venusaur", "Seed", 3, "Grass and Poison"

Victreebel = Pokemon()
Victreebel.name, Victreebel.kind, Victreebel.number, Victreebel.typing = "Victreebel", "Flycatcher", 71, "Grass and Poison"

Vileplume = Pokemon()
Vileplume.name, Vileplume.kind, Vileplume.number, Vileplume.typing = "Vileplume", "Flower", 45, "Grass and Poison"

Voltorb = Pokemon()
Voltorb.name, Voltorb.kind, Voltorb.number, Voltorb.typing = "Voltorb", "Ball", 100, "Electric"

Vulpix = Pokemon()
Vulpix.name, Vulpix.kind, Vulpix.number, Vulpix.typing = "Vulpix", "Fox", 37, "Fire"

#W Pokemon Classifications
Wartortle = Pokemon()
Wartortle.name, Wartortle.kind, Wartortle.number, Wartortle.typing = "Wartortle", "Turtle", 8, "Water"

Weedle = Pokemon()
Weedle.name, Weedle.kind, Weedle.number, Weedle.typing = "Weedle", "Hairy Bug", 13, "Bug and Poison"

Weepinbell = Pokemon()
Weepinbell.name, Weepinbell.kind, Weepinbell.number, Weepinbell.typing = "Weepinbell", "Flycatcher", 70, "Grass and Poison"

Weezing = Pokemon()
Weezing.name, Weezing.kind, Weezing.number, Weezing.typing = "Weezing", "Poison Gas", 110, "Poison"

Wigglytuff = Pokemon()
Wigglytuff.name, Wigglytuff.kind, Wigglytuff.number, Wigglytuff.typing = "Wigglytuff", "Balloon", 40, "Normal and Fairy"

#Z Pokemon Classifications
Zapdos = Pokemon()
Zapdos.name, Zapdos.kind, Zapdos.number, Zapdos.typing = "Zapdos", "Electric", 145, "Electric and Flying"

Zubat = Pokemon()
Zubat.name, Zubat.kind, Zubat.number, Zubat.typing = "Zubat", "Bat", 41, "Poison and Flying"

#Error message
def error():
	print("This Pokemon is either not a Kanto Pokemon or doesn't exist.")

#Allows program to run indefinitely
while True:
	#Asks for input
	Pokemon = input("Which Pokemon would you like to learn about? ")
	#This makes it so the input is turned into all lowercase letters, expediting the process.
	Pokemon = Pokemon.lower()
	#Allows user to exit program
	if Pokemon == "quit" or Pokemon == "end" or Pokemon == "stop" or Pokemon == "quit()":
		print("Closing program. Thank you for using this program!")
		break
	#Detects Pokemon that start with A
	if Pokemon[0] == "a":
		if Pokemon == "abra":
			print(Abra.desc())
		elif Pokemon == "aerodactyl":
			print(Aerodactyl.desc())
		elif Pokemon == "alakazam":
			print(Alakazam.desc())
		elif Pokemon == "arbok":
			print(Arbok.desc())
		elif Pokemon == "arcanine":
			print(Arcanine.desc())
		elif Pokemon == "articuno":
			print(Articuno.desc())
		else:
			error()

	#Detects Pokemon that start with B
	elif Pokemon[0] == "b":
		if Pokemon == "beedrill":
			print(Beedrill.desc())
		elif Pokemon == "bellsprout":
			print(Bellsprout.desc())
		elif Pokemon == "blastoise":
			print(Blastoise.desc())
		elif Pokemon == "bulbasaur":
			print(Bulbasaur.desc())
		elif Pokemon == "butterfree":
			print(Butterfree.desc())
		else:
			error()

	#Detects Pokemon that start with C
	elif Pokemon[0] == "c":
		if Pokemon == "caterpie":
			print(Caterpie.desc())
		elif Pokemon == "chansey":
			print(Chansey.desc())
		elif Pokemon == "charizard":
			print(Charizard.desc())
		elif Pokemon == "charmander":
			print(Charmander.desc())
		elif Pokemon == "charmeleon":
			print(Charmeleon.desc())
		elif Pokemon == "clefable":
			print(Clefable.desc())
		elif Pokemon == "clefairy":
			print(Clefairy.desc())
		elif Pokemon == "cloyster":
			print(Cloyster.desc())
		elif Pokemon == "cubone":
			print(Cubone.desc())
		else:
			error()

	#Detects Pokemon that start with D
	elif Pokemon[0] == "d":
		if Pokemon == "dewgong":
			print(Dewgong.desc())
		elif Pokemon == "diglett":
			print(Diglett.desc())
		elif Pokemon == "ditto":
			print(Ditto.desc())
		elif Pokemon == "dodrio":
			print(Dodrio.desc())
		elif Pokemon == "doduo":
			print(Doduo.desc())
		elif Pokemon == "dragonair":
			print(Dragonair.desc())
		elif Pokemon == "dragonite":
			print(Dragonite.desc())
		elif Pokemon == "dratini":
			print(Dratini.desc())
		elif Pokemon == "drowzee":
			print(Drowzee.desc())
		elif Pokemon == "dugtrio":
			print(Dugtrio.desc())
		else:
			error()

	#Detects Pokemon that start with E
	elif Pokemon[0] == "e":
		if Pokemon == "eevee":
			print(Eevee.desc())
		elif Pokemon == "ekans":
			print(Ekans.desc())
		elif Pokemon == "electabuzz":
			print(Electabuzz.desc())
		elif Pokemon == "electrode":
			print(Electrode.desc())
		elif Pokemon == "exeggcute":
			print(Exeggcute.desc())
		elif Pokemon == "exeggutor":
			print(Exeggutor.desc())
		else:
			error()

	#Detects Pokemon that start with F
	elif Pokemon[0] ==  "f":
		if Pokemon == "farfetchd" or Pokemon == "farfetch'd":
			print(Farfetchd.desc())
		elif Pokemon == "fearow":
			print(Fearow.desc())
		elif Pokemon == "flareon":
			print(Flareon.desc())
		else:
			error()

	#Detects Pokemon that start with G
	elif Pokemon[0] == "g":
		if Pokemon == "gastly":
			print(Gastly.desc())
		elif Pokemon == "gengar":
			print(Gengar.desc())
		elif Pokemon == "geodude":
			print(Geodude.desc())
		elif Pokemon == "gloom":
			print(Gloom.desc())
		elif Pokemon == "golbat":
			print(Golbat.desc())
		elif Pokemon == "goldeen":
			print(Goldeen.desc())
		elif Pokemon == "golduck":
			print(Golduck.desc())
		elif Pokemon == "golem":
			print(Golem.desc())
		elif Pokemon == "graveler":
			print(Graveler.desc())
		elif Pokemon == "grimer":
			print(Grimer.desc())
		elif Pokemon == "growlithe":
			print(Growlithe.desc())
		elif Pokemon == "gyarados":
			print(Gyarados.desc())
		else:
			error()

	#Detects Pokemon that start with H
	elif Pokemon[0] == "h":
		if Pokemon == "haunter":
			print(Haunter.desc())
		elif Pokemon == "hitmonchan":
			print(Hitmonchan.desc())
		elif Pokemon == "hitmonlee":
			print(Hitmonlee.desc())
		elif Pokemon == "horsea":
			print(Horsea.desc())
		elif Pokemon ==  "hypno":
			print(Hypno.desc())
		else:
			error()

	#Detects Pokemon that start with I
	elif Pokemon[0]  == "i":
		if Pokemon == "ivysaur":
			print(Ivysaur.desc())
		else:
			error()

	#Detects Pokemon that start with J
	elif Pokemon[0] == "j":
		if Pokemon == "jigglypuff":
			print(Jigglypuff.desc())
		elif Pokemon == "jolteon":
			print(Jolteon.desc())
		elif Pokemon == "jynx":
			print(Jynx.desc())
		else:
			error()

	#Detects Pokemon that start with K
	elif Pokemon[0] == "k":
		if Pokemon == "kabuto":
			print(Kabuto.desc())
		elif Pokemon == "kabutops":
			print(Kabutops.desc())
		elif Pokemon == "kadabra":
			print(Kadabra.desc())
		elif Pokemon == "kakuna":
			print(Kakuna.desc())
		elif Pokemon == "kangaskhan":
			print(Kangaskhan.desc())
		elif Pokemon == "kingler":
			print(Kingler.desc())
		elif Pokemon == "koffing":
			print(Koffing.desc())
		elif Pokemon == "krabby":
			print(Krabby.desc())
		else:
			error()

	#Detects Pokemon that start with L
	elif Pokemon[0] == "l":
		if Pokemon == "lapras":
			print(Lapras.desc())
		elif Pokemon == "lickitung":
			print(Lickitung.desc())
		else:
			error()

	#Detects Pokemon that start with M
	elif Pokemon[0] == "m":
		if Pokemon == "machamp":
			print(Machamp.desc())
		elif Pokemon == "machoke":
			print(Machoke.desc())
		elif Pokemon == "machop":
			print(Machop.desc())
		elif Pokemon == "magikarp":
			print(Magikarp.desc())
		elif Pokemon ==	"magmar":
			print(Magmar.desc())
		elif Pokemon == "magnemite":
			print(Magnemite.desc())
		elif Pokemon == "magneton":
			print(Magneton.desc())
		elif Pokemon == "mankey":
			print(Mankey.desc())
		elif Pokemon == "marowak":
			print(Marowak.desc())
		elif Pokemon == "meowth":
			print(Meowth.desc())
		elif Pokemon == "metapod":
			print(Metapod.desc())
		elif Pokemon == "mew":
			print(Mew.desc())
		elif Pokemon == "mewtwo":
			print(Mewtwo.desc())
		elif Pokemon == "moltres":
			print(Moltres.desc())
		elif Pokemon == "mr mime" or Pokemon == "mrmime" or Pokemon == "mr. mime":
			print(MrMime.desc())
		elif Pokemon == "muk":
			print(Muk.desc())	
		else:
			error()

	#Detects Pokemon that start with N
	elif Pokemon[0] == "n":
		if Pokemon == "nidoking":
			print(Nidoking.desc())
		elif Pokemon == "nidoqueen":
			print(Nidoqueen.desc())
		elif Pokemon == "nidoran":
			print(Nidoran.desc())
		elif Pokemon == "nidorina":
			print(Nidorina.desc())
		elif Pokemon == "nidorino":
			print(Nidorino.desc())
		elif Pokemon == "ninetales":
			print(Ninetales.desc())
		else:
			error()

	#Detects Pokemon that start with O
	elif Pokemon[0] == "o":
		if Pokemon == "oddish":
			print(Oddish.desc())
		elif Pokemon == "omanyte":
			print(Omanyte.desc())
		elif Pokemon == "omastar":
			print(Omastar.desc())
		elif Pokemon == "onix":
			print(Onix.desc())
		else:
			error()

	#Detects Pokemon that start with P
	elif Pokemon[0] == "p":
		if Pokemon == "paras":
			print(Paras.desc())
		elif Pokemon == "parasect":
			print(Parasect.desc())
		elif Pokemon == "persian":
			print(Persian.desc())
		elif Pokemon == "pidgeot":
			print(Pidgeot.desc())
		elif Pokemon == "pidgeotto":
			print(Pidgeotto.desc())
		elif Pokemon == "pidgey":
			print(Pidgey.desc())
		elif Pokemon == "pikachu":
			print(Pikachu.desc())
		elif Pokemon == "pinsir":
			print(Pinsir.desc())
		elif Pokemon == "poliwag":
			print(Poliwag.desc())
		elif Pokemon == "poliwhirl":
			print(Poliwhirl.desc())
		elif Pokemon == "poliwrath":
			print(Poliwrath.desc())
		elif Pokemon == "ponyta":
			print(Ponyta.desc())
		elif Pokemon == "porygon":
			print(Porygon.desc())
		elif Pokemon == "primeape":
			print(Primeape.desc())
		elif Pokemon == "psyduck":
			print(Psyduck.desc())

	#Detects Pokemon that start with R
	elif Pokemon[0] == "r":
		if Pokemon == "raichu":
			print(Raichu.desc())
		elif Pokemon == "rapidash":
			print(Rapidash.desc())
		elif Pokemon == "rattata":
			print(Rattata.desc())
		elif Pokemon == "raticate":
			print(Raticate.desc())
		elif Pokemon == "rhydon":
			print(Rhydon.desc())
		elif Pokemon == "rhyhorn":
			print(Rhyhorn.desc())
		else:
			error()

	#Detects Pokemon that start with S
	elif Pokemon[0] == "s":
		if Pokemon == "sandshrew":
			print(Sandshrew.desc())
		elif Pokemon == "sandslash":
			print(Sandslash.desc())
		elif Pokemon == "scyther":
			print(Scyther.desc())
		elif Pokemon == "seadra":
			print(Seadra.desc())
		elif Pokemon == "seel":
			print(Seel.desc())
		elif Pokemon == "shellder":
			print(Shellder.desc())
		elif Pokemon == "slowbro":
			print(Slowbro.desc())
		elif Pokemon == "slowpoke":
			print(Slowpoke.desc())
		elif Pokemon == "snorlax":
			print(Snorlax.desc())
		elif Pokemon == "spearow":
			print(Spearow.desc())
		elif Pokemon == "squirtle":
			print(Squirtle.desc())
		elif Pokemon == "starmie":
			print(Starmie.desc())
		elif Pokemon == "staryu":
			print(Staryu.desc())
		else:
			error()

	#Detects Pokemon that start with T
	elif Pokemon[0] == "t":
		if Pokemon == "tangela":
			print(Tangela.desc())
		elif Pokemon == "tauros":
			print(Tauros.desc())
		elif Pokemon == "tentacool":
			print(Tentacool.desc())
		elif Pokemon == "tentacruel":
			print(Tentacruel.desc())
		else:
			error()

	#Detects Pokemon that start with V
	elif Pokemon[0] == "v":
		if Pokemon == "vaporeon":
			print(Vaporeon.desc())
		elif Pokemon == "venomoth":
			print(Venomoth.desc())
		elif Pokemon == "venonat":
			print(Venonat.desc())
		elif Pokemon == "venusaur":
			print(Venusaur.desc())
		elif Pokemon == "victreebel":
			print(Victreebel.desc())
		elif Pokemon == "vileplume":
			print(Vileplume.desc())
		elif Pokemon == "voltorb":
			print(Voltorb.desc())
		elif Pokemon == "vulpix":
			print(Vulpix.desc())
		else:
			error()

	#Detects Pokemon that start with W
	elif Pokemon[0] == "w":
		if Pokemon == "wartortle":
			print(Wartortle.desc())
		elif Pokemon == "weedle":
			print(Weedle.desc())
		elif Pokemon == "weepinbell":
			print(Weepinbell.desc())
		elif Pokemon == "weezing":
			print(Weezing.desc())
		elif Pokemon ==  "wigglytuff":
			print(Wigglytuff.desc())
		else:
			error()

	#Detects Pokemon that start with Z
	elif Pokemon[0] == "z":
		if Pokemon == "zapdos":
			print(Zapdos.desc())
		elif Pokemon == "zubat":
			print(Zubat.desc())
		else:
			error()

	#Final error message
	else:
		error()