# Attack Speed (Saldırı Hızı) değerleri

Kural: yakın saldırıda **savunanın Saldırı Hızı saldıranınkinden büyükse savunan önce vurur** (eski Gnoll Marauder seçeneği 996'nın yerine). Eşitse ya da küçükse normal sıra.
Önce vurma olmaz: saldıranda "karşılık alınmaz" yeteneği varsa (Vampire Lord gibi), saldıran savaş makinesiyse, savunanın karşılık hakkı kalmadıysa, savunan kör / taşlaşmış / felçliyse. Sınırsız karşılık vuranlar (Griffin gibi) her saldırıda önce vurabilir.

Ölçek 1-10. Değiştirmek istediğin değerleri **Saldırı Hızı** sütununda değiştir; script değerleri bu dosyadan alacak.
Süvariler (Cavalier, Champion, Holy Champion): saldırırken uzaktan hücum ederse tam değer; komşu hücredeki düşmana saldırırsa ya da savunmadaysa değerin yarısı (aşağı yuvarlanır).
Hız = yaratığın normal savaş hızı (karşılaştırma için). Savaş makineleri ve boş (NOT USED) yaratıklar listede yok.

## Castle

| ID | Yaratık | Seviye | Hız | Saldırı Hızı | Neden |
|---:|---|:---:|:---:|:---:|---|
| 0 | Pikeman | 1 | 4 | **7** | uzun mızrak, saldıranı erken karşılar |
| 1 | Halberdier | 1 | 5 | **7** | uzun mızrak, saldıranı erken karşılar |
| 197 | Royal Halberdier | 1 | 6 | **8** | uzun mızrak, geliştirilmiş |
| 2 | Archer | 2 | 4 | **4** | okçu, yakında yavaş |
| 3 | Marksman | 2 | 6 | **5** | okçu, çevik |
| 198 | Crossbowman | 2 | 7 | **4** | okçu, yakında yavaş |
| 4 | Griffin | 3 | 6 | **6** | hızlı pençe |
| 5 | Royal Griffin | 3 | 9 | **7** | hızlı pençe |
| 199 | Cesar Griffin | 3 | 10 | **8** | çok hızlı pençe |
| 301 | Squire | 3 | 5 | **5** | ortalama kılıç |
| 302 | Man at Arms | 3 | 6 | **5** | ortalama kılıç |
| 6 | Swordsman | 4 | 5 | **5** | ortalama kılıç |
| 7 | Crusader | 4 | 6 | **6** | usta kılıç |
| 291 | Inquisitor | 4 | 8 | **6** | usta kılıç |
| 292 | Thunder Warrior | 4 | 8 | **8** | yıldırım savaşçı |
| 8 | Monk | 5 | 5 | **4** | rahip, dövüşçü değil |
| 9 | Zealot | 5 | 7 | **4** | rahip, dövüşçü değil |
| 320 | High Priest | 5 | 7 | **4** | rahip, dövüşçü değil |
| 340 | Swordmaster | 5 | 8 | **9** | kılıç ustası |
| 10 | Cavalier | 6 | 7 | **7** | süvari mızrağı: saldırıda uzaktan hücum ederse tam değer, komşuya saldırırsa ya da savunmadaysa yarısı |
| 11 | Champion | 6 | 9 | **8** | süvari mızrağı: saldırıda uzaktan hücum ederse tam değer, komşuya saldırırsa ya da savunmadaysa yarısı |
| 201 | Holy Champion | 6 | 12 | **8** | süvari mızrağı: saldırıda uzaktan hücum ederse tam değer, komşuya saldırırsa ya da savunmadaysa yarısı |
| 318 | Archer Rider | 6 | 7 | **6** | atlı okçu |
| 12 | Angel | 7 | 12 | **9** | hızlı ve zarif |
| 13 | Archangel | 7 | 18 | **9** | hızlı ve zarif |
| 202 | Seraph | 7 | 20 | **10** | göksel hız |
| 269 | Light Templar | 7 | 5 | **4** | ağır zırhlı |
| 278 | Light Paladin | 7 | 7 | **4** | ağır zırhlı |
| 150 | Supreme Archangel | 8 | 18 | **10** | göksel hız |

## Rampart

| ID | Yaratık | Seviye | Hız | Saldırı Hızı | Neden |
|---:|---|:---:|:---:|:---:|---|
| 14 | Centaur | 1 | 6 | **5** | atlı okçu |
| 15 | Centaur Captain | 1 | 8 | **6** | atlı okçu |
| 293 | Centaur General | 1 | 10 | **7** | centaur komutanı |
| 16 | Dwarf | 2 | 3 | **3** | kısa ve ağır |
| 17 | Battle Dwarf | 2 | 5 | **4** | kısa ve ağır |
| 203 | Berserker Dwarf | 2 | 6 | **6** | berserk öfkesi |
| 18 | Wood Elf | 3 | 6 | **6** | çevik elf |
| 19 | Grand Elf | 3 | 7 | **7** | çevik elf |
| 256 | Sharpshooter Elf | 3 | 7 | **7** | çevik elf |
| 20 | Pegasus | 4 | 8 | **7** | hızlı kanatlı at |
| 21 | Silver Pegasus | 4 | 12 | **8** | hızlı kanatlı at |
| 204 | Golden Pegasus | 4 | 15 | **8** | hızlı kanatlı at |
| 270 | Dryad | 4 | 6 | **6** | çevik orman ruhu |
| 279 | Oak Dryad | 4 | 8 | **6** | çevik orman ruhu |
| 22 | Dendroid Guard | 5 | 3 | **2** | ağaç, çok yavaş |
| 23 | Dendroid Soldier | 5 | 4 | **2** | ağaç, çok yavaş |
| 205 | Elder Dendroid | 5 | 5 | **3** | ağaç, yavaş |
| 24 | Unicorn | 6 | 7 | **6** | boynuz, hızlı |
| 25 | War Unicorn | 6 | 9 | **7** | boynuz, hızlı |
| 206 | Legendary Unicorn | 6 | 10 | **7** | boynuz, hızlı |
| 26 | Green Dragon | 7 | 10 | **5** | iri ejderha |
| 27 | Gold Dragon | 7 | 16 | **6** | iri ejderha |
| 207 | Pure Diamond Dragon | 7 | 20 | **6** | iri ejderha |
| 349 | Forest Spirit | 7 | 10 | **4** | iri orman ruhu |
| 350 | Spring Spirit | 7 | 12 | **4** | iri orman ruhu |
| 151 | Diamond Dragon | 8 | 16 | **6** | iri ejderha |

## Tower

| ID | Yaratık | Seviye | Hız | Saldırı Hızı | Neden |
|---:|---|:---:|:---:|:---:|---|
| 28 | Gremlin | 1 | 4 | **4** | küçük, beceriksiz |
| 29 | Master Gremlin | 1 | 5 | **4** | küçük, beceriksiz |
| 255 | Grandmaster Gremlin | 1 | 5 | **5** | küçük, beceriksiz |
| 30 | Stone Gargoyle | 2 | 6 | **4** | taş |
| 31 | Obsidian Gargoyle | 2 | 9 | **5** | taş, hızlı kanat |
| 208 | Marble Gargoyle | 2 | 10 | **5** | taş, hızlı kanat |
| 32 | Stone Golem | 3 | 3 | **1** | taş golem, çok yavaş |
| 33 | Iron Golem | 3 | 5 | **2** | metal golem |
| 209 | Steel Golem | 3 | 6 | **2** | metal golem |
| 34 | Mage | 4 | 5 | **3** | büyücü, dövüşçü değil |
| 35 | Arch Mage | 4 | 7 | **3** | büyücü, dövüşçü değil |
| 257 | Supreme Arch Mage | 4 | 9 | **3** | büyücü, dövüşçü değil |
| 36 | Genie | 5 | 7 | **7** | cin, çok hızlı |
| 37 | Master Genie | 5 | 11 | **8** | cin, çok hızlı |
| 210 | Arcane Genie | 5 | 13 | **8** | cin, çok hızlı |
| 38 | Naga | 6 | 5 | **6** | altı kollu kılıç |
| 39 | Naga Queen | 6 | 7 | **7** | altı kollu kılıç |
| 211 | Naga Rakshasa | 6 | 9 | **7** | altı kollu kılıç |
| 40 | Giant | 7 | 7 | **3** | dev, ağır |
| 41 | Titan | 7 | 11 | **3** | dev, ağır |
| 212 | Guardian of Zeus | 7 | 15 | **6** | dev, ağır |
| 271 | Drake Golem | 7 | 9 | **2** | metal golem |
| 280 | Dragon Golem | 7 | 15 | **3** | ejderha golem |
| 152 | Lord of Thunder | 8 | 12 | **6** | dev, ağır |

## Inferno

| ID | Yaratık | Seviye | Hız | Saldırı Hızı | Neden |
|---:|---|:---:|:---:|:---:|---|
| 42 | Imp | 1 | 5 | **6** | küçük, çevik |
| 43 | Familiar | 1 | 7 | **7** | küçük, çevik |
| 213 | Vermin | 1 | 9 | **8** | küçük, çevik |
| 44 | Gog | 2 | 4 | **4** | okçu, yakında yavaş |
| 45 | Magog | 2 | 6 | **4** | okçu, yakında yavaş |
| 214 | Winged Magog | 2 | 7 | **5** | okçu, kanatlı |
| 46 | Hell Hound | 3 | 7 | **7** | hızlı köpek |
| 47 | Cerberus | 3 | 8 | **7** | hızlı köpek |
| 215 | Astral Cerberi | 3 | 9 | **8** | hızlı köpek |
| 48 | Demon | 4 | 5 | **4** | sıradan iblis |
| 49 | Horned Demon | 4 | 6 | **5** | sıradan iblis |
| 216 | Sharp-Horned Demon | 4 | 8 | **6** | çift saldırı, çevik |
| 272 | Succubus | 4 | 7 | **7** | çevik, uçan |
| 281 | Lilim | 4 | 11 | **8** | çevik, uçan |
| 50 | Pit Fiend | 5 | 6 | **5** | ağır iblis |
| 51 | Pit Lord | 5 | 7 | **5** | ağır iblis |
| 217 | Pit Master | 5 | 8 | **6** | ağır iblis |
| 52 | Efreeti | 6 | 9 | **7** | ateş cini, hızlı |
| 53 | Efreet Sultan | 6 | 13 | **7** | ateş cini, hızlı |
| 218 | Efreeti Rajah | 6 | 15 | **9** | ateş cini, hızlı |
| 54 | Devil | 7 | 11 | **7** | şeytan, hızlı |
| 55 | Arch Devil | 7 | 17 | **8** | şeytan, hızlı |
| 219 | Antichrist | 7 | 19 | **9** | şeytan, hızlı |
| 337 | Fiend of Tartarus | 7 | 12 | **5** | ağır iblis |
| 338 | Lord of Tartarus | 7 | 18 | **6** | ağır iblis |
| 153 | Hell Baron | 8 | 17 | **9** | şeytan, hızlı |

## Necropolis

| ID | Yaratık | Seviye | Hız | Saldırı Hızı | Neden |
|---:|---|:---:|:---:|:---:|---|
| 56 | Skeleton | 1 | 4 | **3** | iskelet |
| 57 | Skeleton Warrior | 1 | 5 | **4** | iskelet savaşçı |
| 220 | Skeleton Knight | 1 | 5 | **5** | iskelet şövalye |
| 58 | Walking Dead | 2 | 3 | **1** | zombi, çok yavaş |
| 59 | Zombie | 2 | 4 | **1** | zombi, çok yavaş |
| 60 | Wight | 3 | 5 | **5** | hayalet |
| 61 | Wraith | 3 | 7 | **6** | hayalet |
| 261 | Specter | 3 | 8 | **6** | hayalet |
| 329 | Ghoul | 3 | 6 | **3** | hortlak yiyici |
| 62 | Vampire | 4 | 6 | **7** | vampir, hızlı |
| 63 | Vampire Lord | 4 | 9 | **8** | vampir, hızlı |
| 194 | Dire Werewolf | 4 | 7 | **8** | kurt adam, hızlı |
| 221 | Nosferatu | 4 | 10 | **8** | vampir, hızlı |
| 273 | Werewolf | 4 | 5 | **7** | kurt adam |
| 299 | Sharpshooter Skeleton | 4 | 9 | **4** | iskelet savaşçı |
| 64 | Lich | 5 | 6 | **2** | büyücü, dövüşçü değil |
| 65 | Power Lich | 5 | 7 | **2** | büyücü, dövüşçü değil |
| 222 | Lich King | 5 | 8 | **3** | büyücü, dövüşçü değil |
| 66 | Black Knight | 6 | 7 | **5** | ağır şövalye |
| 67 | Dread Knight | 6 | 9 | **6** | ağır şövalye |
| 223 | Death Knight | 6 | 10 | **6** | ağır şövalye |
| 68 | Bone Dragon | 7 | 9 | **3** | iskelet ejderha, ağır |
| 69 | Ghost Dragon | 7 | 14 | **4** | iskelet ejderha |
| 224 | Red Bones Dragon | 7 | 18 | **4** | iskelet ejderha |
| 325 | Shadow Dragon | 7 | 9 | **5** | kan ejderhası |
| 331 | Dark Templar | 7 | 5 | **4** | ağır zırhlı |
| 332 | Dark Paladin | 7 | 8 | **4** | ağır zırhlı |
| 154 | Blood Dragon | 8 | 14 | **5** | kan ejderhası |

## Dungeon

| ID | Yaratık | Seviye | Hız | Saldırı Hızı | Neden |
|---:|---|:---:|:---:|:---:|---|
| 70 | Troglodyte | 1 | 4 | **6** | küçük, sıradan |
| 71 | Infernal Troglodyte | 1 | 5 | **6** | küçük, sıradan |
| 225 | Phosphorescent Troglodyte | 1 | 6 | **7** | küçük, sıradan |
| 72 | Harpy | 2 | 6 | **8** | hızlı pençe |
| 73 | Harpy Hag | 2 | 9 | **9** | çok hızlı pençe |
| 227 | Harpy Sanguinary | 2 | 10 | **9** | çok hızlı pençe |
| 74 | Beholder | 3 | 5 | **2** | göz, dövüşçü değil |
| 75 | Evil Eye | 3 | 7 | **2** | göz, dövüşçü değil |
| 226 | Monstrous Eye | 3 | 7 | **3** | göz, dövüşçü değil |
| 76 | Medusa | 4 | 5 | **4** | okçu, yakında yavaş |
| 77 | Medusa Queen | 4 | 6 | **5** | okçu, yakında yavaş |
| 228 | Medusa Empress | 4 | 8 | **5** | okçu, yakında yavaş |
| 78 | Minotaur | 5 | 6 | **5** | güçlü balta |
| 79 | Minotaur King | 5 | 8 | **6** | güçlü balta |
| 229 | Black Minotaur | 5 | 8 | **6** | güçlü balta |
| 274 | Illithid | 5 | 5 | **4** | büyücü |
| 282 | Alhoon | 5 | 6 | **4** | büyücü |
| 80 | Manticore | 6 | 7 | **6** | hızlı kuyruk |
| 81 | Scorpicore | 6 | 11 | **7** | hızlı kuyruk |
| 230 | Chimera | 6 | 13 | **7** | hızlı kuyruk |
| 82 | Red Dragon | 7 | 11 | **5** | iri ejderha |
| 83 | Black Dragon | 7 | 15 | **6** | iri ejderha |
| 231 | Chasm Dragon | 7 | 20 | **6** | iri ejderha |
| 351 | Lady Spider | 7 | 9 | **7** | örümcek, hızlı |
| 352 | Priestess Spider | 7 | 11 | **7** | örümcek, hızlı |
| 155 | Darkness Dragon | 8 | 15 | **6** | iri ejderha |

## Stronghold

| ID | Yaratık | Seviye | Hız | Saldırı Hızı | Neden |
|---:|---|:---:|:---:|:---:|---|
| 84 | Goblin | 1 | 5 | **6** | küçük, çevik |
| 85 | Hobgoblin | 1 | 7 | **7** | küçük, çevik |
| 232 | Hobgoblin Overlord | 1 | 7 | **7** | küçük, çevik |
| 86 | Wolf Rider | 2 | 6 | **8** | kurt, çok hızlı |
| 87 | Wolf Raider | 2 | 8 | **9** | kurt, çok hızlı |
| 233 | Wolf Rider Killer | 2 | 9 | **9** | kurt, çok hızlı |
| 88 | Orc | 3 | 4 | **4** | okçu, yakında yavaş |
| 89 | Orc Chieftain | 3 | 5 | **5** | okçu, yakında yavaş |
| 234 | Orc Leader | 3 | 7 | **5** | okçu, yakında yavaş |
| 90 | Ogre | 4 | 4 | **2** | ağır, hantal |
| 91 | Ogre Mage | 4 | 5 | **3** | ağır, hantal |
| 235 | Elder Ogre | 4 | 6 | **3** | ağır, hantal |
| 92 | Roc | 5 | 7 | **5** | iri kuş |
| 93 | Thunderbird | 5 | 11 | **6** | iri kuş |
| 236 | Lightningbird | 5 | 13 | **7** | şimşek kuşu, hızlı |
| 94 | Cyclops | 6 | 6 | **3** | dev, ağır |
| 95 | Cyclops King | 6 | 8 | **3** | dev, ağır |
| 237 | Cyclops Emperor | 6 | 10 | **4** | dev, ağır |
| 275 | Coatl | 6 | 11 | **7** | yılan, hızlı |
| 283 | Quetzalcoatl | 6 | 15 | **8** | yılan, çok hızlı |
| 96 | Behemoth | 7 | 6 | **3** | iri ve ağır |
| 97 | Ancient Behemoth | 7 | 9 | **4** | iri ve ağır |
| 238 | Spectral Behemoth | 7 | 18 | **7** | hayalet behemoth |
| 156 | Ghost Behemoth | 8 | 11 | **7** | hayalet behemoth |

## Fortress

| ID | Yaratık | Seviye | Hız | Saldırı Hızı | Neden |
|---:|---|:---:|:---:|:---:|---|
| 98 | Gnoll | 1 | 4 | **5** | sıradan |
| 99 | Gnoll Marauder | 1 | 5 | **5** | sıradan |
| 321 | Gnoll Shaman | 1 | 6 | **4** | şaman |
| 100 | Lizardman | 2 | 4 | **4** | okçu, yakında yavaş |
| 101 | Lizard Warrior | 2 | 5 | **5** | okçu / sıradan savaşçı |
| 239 | Centagnoll | 2 | 10 | **7** | çevik |
| 240 | Elite Lizard | 2 | 6 | **5** | okçu / sıradan savaşçı |
| 326 | Lizard Soldier | 2 | 7 | **5** | okçu / sıradan savaşçı |
| 102 | Gorgon | 3 | 5 | **2** | iri ve ağır |
| 103 | Mighty Gorgon | 3 | 6 | **3** | iri ve ağır |
| 241 | Chaotic Dragon Fly | 3 | 15 | **9** | sinek, çok hızlı |
| 104 | Serpent Fly | 4 | 9 | **8** | sinek, çok hızlı |
| 105 | Dragon Fly | 4 | 13 | **9** | sinek, çok hızlı |
| 242 | Lava Basilisk | 4 | 9 | **5** | kertenkele |
| 106 | Basilisk | 5 | 5 | **4** | kertenkele |
| 107 | Greater Basilisk | 5 | 7 | **5** | kertenkele |
| 244 | Catoblepas | 5 | 8 | **3** | iri ve ağır |
| 276 | Troll Hag | 5 | 6 | **4** | trol cadısı |
| 284 | Troll Witch | 5 | 7 | **5** | trol cadısı |
| 108 | Wyvern | 6 | 7 | **6** | hızlı kuyruk |
| 109 | Wyvern Monarch | 6 | 11 | **7** | hızlı kuyruk |
| 243 | Acid Wyvern | 6 | 14 | **7** | hızlı kuyruk |
| 110 | Hydra | 7 | 5 | **2** | çok başlı, ağır |
| 111 | Chaos Hydra | 7 | 7 | **3** | çok başlı, ağır |
| 245 | Nightmare Hydra | 7 | 10 | **4** | çok başlı |
| 353 | Sea Serpent | 7 | 9 | **5** | deniz yılanı |
| 354 | Leviathan | 7 | 12 | **5** | deniz yılanı |
| 157 | Hell Hydra | 8 | 10 | **3** | çok başlı, ağır |

## Conflux

| ID | Yaratık | Seviye | Hız | Saldırı Hızı | Neden |
|---:|---|:---:|:---:|:---:|---|
| 118 | Pixie | 1 | 7 | **8** | küçük, çok hızlı |
| 119 | Sprite | 1 | 9 | **9** | küçük, çok hızlı |
| 246 | Fairy | 1 | 10 | **9** | küçük, çok hızlı |
| 112 | Air Elemental | 2 | 7 | **8** | hava, çok hızlı |
| 127 | Storm Elemental | 2 | 8 | **8** | hava, çok hızlı |
| 247 | Hurricane Elemental | 2 | 10 | **9** | hava, çok hızlı |
| 115 | Water Elemental | 3 | 5 | **5** | su |
| 123 | Ice Elemental | 3 | 6 | **5** | su |
| 248 | Life Elemental | 3 | 8 | **5** | su |
| 277 | Triton | 3 | 6 | **6** | triton |
| 285 | Abyssal Triton | 3 | 8 | **7** | triton |
| 114 | Fire Elemental | 4 | 6 | **6** | ateş, hızlı |
| 129 | Energy Elemental | 4 | 8 | **7** | ateş, hızlı |
| 249 | Plasma Elemental | 4 | 10 | **7** | ateş, hızlı |
| 113 | Earth Elemental | 5 | 4 | **2** | toprak, ağır |
| 125 | Magma Elemental | 5 | 6 | **3** | lav / magma, ağır |
| 250 | Lava Elemental | 5 | 8 | **3** | lav / magma, ağır |
| 120 | Psychic Elemental | 6 | 7 | **6** | elemental |
| 121 | Magic Elemental | 6 | 9 | **6** | elemental |
| 251 | Void Elemental | 6 | 10 | **7** | elemental |
| 130 | Firebird | 7 | 15 | **8** | ateş kuşu |
| 131 | Phoenix | 7 | 21 | **9** | anka kuşu, çok hızlı |
| 252 | Divine Phoenix | 7 | 25 | **9** | anka kuşu, çok hızlı |
| 122 | Dark Phoenix | 7 | 24 | **10** | kara alevli anka kuşu, ailenin en hızlısı (Forge & Fury, boş yuva 122) |
| 355 | Planeswalker | 7 | 12 | **5** | büyücü |
| 356 | Elementalist | 7 | 15 | **5** | büyücü |
| 158 | Sacred Phoenix | 8 | 21 | **9** | anka kuşu, çok hızlı |
| 116 | Gold Golem | - | 5 | **2** | metal golem |
| 117 | Diamond Golem | - | 5 | **2** | metal golem |

## Neutral

| ID | Yaratık | Seviye | Hız | Saldırı Hızı | Neden |
|---:|---|:---:|:---:|:---:|---|
| 138 | Halfling | 1 | 5 | **6** | küçük, çevik |
| 295 | Skeleton Archer | 1 | 5 | **3** | iskelet |
| 296 | Red Skeleton | 1 | 4 | **3** | iskelet |
| 297 | Mana Skeleton | 1 | 5 | **4** | iskelet savaşçı |
| 300 | Conscript | 1 | 4 | **2** | köylü |
| 303 | Peon | 1 | 4 | **2** | köylü |
| 317 | Will-o-wisp | 1 | 5 | **8** | ışık ruhu |
| 348 | Halfling Grenadier | 1 | 6 | **6** | küçük, çevik |
| 260 | Assassin | 2 | 8 | **9** | suikastçı |
| 264 | Leprechaun | 2 | 5 | **7** | cüce peri |
| 304 | Tortofroid | 2 | 5 | **1** | kaplumbağa |
| 305 | Vile Tortofroid | 2 | 7 | **2** | kaplumbağa |
| 287 | Dread Skipper | 3 | 6 | **5** | korsan |
| 309 | Forest Dragon | 3 | 7 | **6** | küçük ejderha |
| 310 | Swamp Dragon | 3 | 9 | **7** | küçük ejderha |
| 311 | Moss Thrall | 3 | 5 | **3** | yosun |
| 315 | Stump Rider | 3 | 5 | **5** | kütük binici |
| 200 | Dragon Slayer | 4 | 8 | **7** | ejderha avcısı |
| 262 | Satyr | 4 | 7 | **6** | satir |
| 288 | Mermaid | 4 | 5 | **5** | deniz kızı |
| 312 | Ravenous Coctatrice | 4 | 7 | **6** | kokatris |
| 316 | Baba Yaga | 4 | 7 | **4** | cadı |
| 328 | Sacred Elf | 4 | 12 | **8** | çevik elf |
| 341 | Green Dragonling | 4 | 7 | **6** | küçük ejderha |
| 342 | Red Dragonling | 4 | 8 | **6** | küçük ejderha |
| 169 | War Zealot | 5 | 9 | **5** | rahip-savaşçı |
| 263 | Fangarm | 5 | 6 | **5** | fangarm |
| 289 | Fire Paladin | 5 | 8 | **6** | çift saldırı şövalye |
| 290 | Ice Knight | 5 | 8 | **6** | çift saldırı şövalye |
| 294 | Vermilion Bird | 5 | 11 | **7** | kuş |
| 307 | Gigas | 5 | 4 | **3** | dev |
| 308 | Hill Gigas | 5 | 6 | **3** | dev |
| 343 | Faerie Dragonling | 5 | 6 | **7** | küçük ejderha |
| 344 | Rust Dragonling | 5 | 8 | **5** | küçük ejderha |
| 259 | Spelllweaver | 6 | 12 | **5** | büyücü |
| 286 | Demilich | 6 | 11 | **3** | büyücü, dövüşçü değil |
| 306 | Dark Elemental | 6 | 11 | **7** | elemental |
| 324 | Mithril Golem | 6 | 7 | **2** | metal golem |
| 335 | Winged Drake | 6 | 9 | **6** | küçük ejderha |
| 336 | Lesser Dragon | 6 | 9 | **5** | iri ejderha |
| 345 | Azure Dragonling | 6 | 10 | **6** | küçük ejderha |
| 133 | Crystal Dragon | 7 | 16 | **4** | kristal ejderha, ağır |
| 167 | Water Messenger | 7 | 5 | **5** | elemental ulak |
| 253 | Tiamat | 7 | 20 | **4** | çok başlı ejderha |
| 254 | Necross Dragon | 7 | 20 | **4** | çok başlı ejderha |
| 258 | Primal Faerie Dragon | 7 | 20 | **8** | peri ejderhası, çevik |
| 265 | Topaz Crystal Dragon | 7 | 12 | **4** | kristal ejderha, ağır |
| 266 | Amethyst Crystal Dragon | 7 | 14 | **4** | kristal ejderha, ağır |
| 267 | Emerald Crystal Dragon | 7 | 16 | **4** | kristal ejderha, ağır |
| 268 | Sapphire Crystal Dragon | 7 | 18 | **4** | kristal ejderha, ağır |
| 298 | Gold Skeleton | 7 | 7 | **2** | ağır iskelet |
| 313 | Centamonth Hunter | 7 | 7 | **3** | iri ve ağır |
| 314 | Centamonth Thrower | 7 | 7 | **3** | iri ve ağır |
| 319 | Asura | 7 | 15 | **8** | altı kollu kılıç, çok hızlı |
| 322 | Mirage Dragon | 7 | 12 | **6** | ayna ejderha |
| 323 | Mirror Dragon | 7 | 15 | **6** | ayna ejderha |
| 327 | Slithzerikai | 7 | 5 | **3** | naga, ağır |
| 330 | Crimson Dragon | 7 | 19 | **6** | iri ejderha |
| 333 | Fallen Angel | 7 | 14 | **7** | düşmüş melek |
| 334 | Angel of Death | 7 | 14 | **7** | düşmüş melek |
| 339 | Sulfide Dragon | 7 | 20 | **5** | iri ejderha |
| 346 | Fire Dragon | 7 | 25 | **5** | iri ejderha |
| 347 | Ice Dragon | 7 | 25 | **4** | buz ejderhası, iri |
| 132 | Azure Dragon | - | 19 | **5** | iri ejderha |
| 134 | Faerie Dragon | - | 15 | **8** | peri ejderhası, çevik |
| 135 | Rust Dragon | - | 17 | **5** | iri ejderha |
| 136 | Enchanter | - | 9 | **4** | okçu / büyücü |
| 137 | Sharpshooter | - | 9 | **5** | okçu |
| 139 | Peasant | - | 3 | **2** | köylü |
| 140 | Boar | - | 6 | **6** | yaban domuzu |
| 141 | Mummy | - | 5 | **1** | mumya, çok yavaş |
| 142 | Nomad | - | 7 | **7** | göçebe süvari |
| 143 | Rogue | - | 6 | **9** | hırsız, çok çevik |
| 144 | Troll | - | 7 | **4** | trol |
| 159 | Ghost | - | 8 | **7** | hayalet |
| 160 | Emissary of War | - | 4 | **1** | savaşmaz |
| 161 | Emissary of Peace | - | 4 | **1** | savaşmaz |
| 162 | Emissary of Mana | - | 4 | **1** | savaşmaz |
| 163 | Emissary of Lore | - | 4 | **1** | savaşmaz |
| 164 | Fire Messenger | - | 5 | **5** | elemental ulak |
| 165 | Earth Messenger | - | 5 | **5** | elemental ulak |
| 166 | Air Messenger | - | 6 | **5** | elemental ulak |
| 168 | Gorynych | - | 14 | **4** | çok başlı ejderha |
| 170 | Arctic Sharpshooter | - | 9 | **5** | okçu |
| 171 | Lava Sharpshooter | - | 9 | **5** | okçu |
| 172 | Nightmare | - | 9 | **8** | kabus atı |
| 173 | Santa Gremlin | - | 5 | **4** | gremlin |
| 192 | Sylvan Centaur | - | 8 | **6** | atlı okçu |
| 193 | Sorceress | - | 8 | **5** | büyücü |
| 195 | Hell Steed | - | 8 | **8** | kabus atı |
| 196 | Dracolich | - | 16 | **3** | iskelet ejderha, ağır |

## Commanders

| ID | Yaratık | Seviye | Hız | Saldırı Hızı | Neden |
|---:|---|:---:|:---:|:---:|---|
| 174 | Paladin | - | 5 | **6** | komutan: Paladin |
| 175 | Hierophant | - | 5 | **4** | komutan: Hierophant |
| 176 | Temple Guardian | - | 5 | **5** | komutan: Temple Guardian |
| 177 | Succubus | - | 5 | **7** | komutan: Succubus |
| 178 | Soul Eater | - | 5 | **6** | komutan: Soul Eater |
| 179 | Brute | - | 5 | **4** | komutan: Brute |
| 180 | Ogre Leader | - | 5 | **3** | komutan: Ogre Leader |
| 181 | Shaman | - | 5 | **4** | komutan: Shaman |
| 182 | Astral Spirit | - | 5 | **6** | komutan: Astral Spirit |
| 183 | Paladin | - | 5 | **6** | komutan: Paladin |
| 184 | Hierophant | - | 5 | **4** | komutan: Hierophant |
| 185 | Temple Guardian | - | 5 | **5** | komutan: Temple Guardian |
| 186 | Succubus | - | 5 | **7** | komutan: Succubus |
| 187 | Soul Eater | - | 5 | **6** | komutan: Soul Eater |
| 188 | Brute | - | 5 | **4** | komutan: Brute |
| 189 | Ogre Leader | - | 5 | **3** | komutan: Ogre Leader |
| 190 | Shaman | - | 5 | **4** | komutan: Shaman |
| 191 | Astral Spirit | - | 5 | **6** | komutan: Astral Spirit |
