---
title: "Protocole de séquençage de virus Ebola par Nanopore | amplicon, barcoding natif"
keywords: protocol
layout: document
last_updated: Dec 14, 2019
tags: [protocol]
summary:
permalink: ebov/ebov-seq-sop-fr.html
folder: ebov
title_text: "Ebola virus sequencing protocol"
subtitle_text: "Nanopore | amplicon | native barcoding"
document_name: "ARTIC-EBOV-seqSOP-fr"
version: v2.0.1
language: fr
creation_date: 2019-12-06
revision_date: 2019-12-14
forked_from: doi:10.1038/nprot.2017.066
author: Luke Meredith, Josh Quick, Sebastian Lequime, Sophie Gryseels, Audrey Lacroix
citation: "Meredith, Quick *et al.* In Prep."
---

{% include callout.html
type='default'
content='**Overview:** Le protocole suivant est adapté de la méthode présentée dans [Quick et al. (2017) *Nature Protocols* **12:** 1261–1276 doi:10.1038/nprot.2017.066](http://doi.org/10.1038/nprot.2017.066) et traite des amorces, de la préparation et purification des amplicons, puis utilise un protocole tube-unique pour ligaturer la librairie avant de séquencer sur minION.'
%}

<br />

Ce document fait partie de la collection sur le protocole de séquençage du virus Ebola par Nanopore :
: [http://artic.network/ebov/](http://artic.network/ebov/)

#### Documents:

Plan des amorces Ebola :
: [https://github.com/artic-network/primer-schemes/tree/master/ZaireEbola/V3](https://github.com/artic-network/primer-schemes/tree/master/ZaireEbola/V3)

Protocole de séquençage du virus Ebola par Nanopore :
: [http://artic.network/ebov/ebov-seq-sop.html](http://artic.network/ebov/ebov-seq-sop.html)

Ebola virus Nanopore sequencing kit-list :
: [http://artic.network/ebov/ebov-seq-kit.html](http://artic.network/ebov/ebov-seq-kit.html)

<br /><br /><br />

{% include wellcome-trust.html %}

<div class="pagebreak"> </div>

## Préparation

#### Equipements nécessaires :

   |---:|:---
   |3| Cabine portative de préparation d'acides nucléiques ou équivalent
   |4| Vortex 12V
   |4| Centrifugeuse portable Sprout
   |4| Pipette Eppendorf P1000
   |4| Pipette Eppendorf P200
   |4| Pipette Eppendorf P20
   |4| Pipette Eppendorf P2
   |1| Support convertible de tubes 1.5mL/0.6mL
   |2| Fluoromètre Quantus
   |2| Machine miniPCR mini16.
   |2| Support magnétique
{: .compact}

#### Consommables nécessaires :


   |---:|:---
   || Reverse Transcriptase SuperScript IV
   || Q5 Hot Start High-Fidelity 2X Master Mix
   || Amorces Ebola-DRC
   || NEBNext Ultra II End Repair/dA-Tailing Module
   || NEBNext Ultra II Ligation module
   || Quick T4 DNA ligase
   || Ampure XP
   || Nanopore Ligation Sequencing Kit 1D
   || Nanopore Native Barcoding Expansion Kit
   || Nanopore R9.4.1 Flow cell
   || Tubes Eppendorf 1.5mL
   || Barettes de 8-tubes 0.2mL
   || Tubes Falcon 50mL
   || Tubes PCR 0.5ml
   || Système QuantiFluor ONE dsDNA
   || Eau nuclease-free
   || Tris 1M pH8
   || Ethanol à 70%
   || Cônes de pipette P1000
   || Cônes de pipette P200
   || Cônes de pipette P10 long (long-reach)
   || Papier absorbant
   || Conteneurs de déchets médicaux tranchants
{: .compact}

#### Recommandations de sécurité, de confinement et de contamination

   |---:|:---
   || Robe de laboratoire hydrophobe à nouer dans le dos
   || Gants
   || Stérilisateurs à lumière UV
   || Lingettes de décontamination
   || Réactifs DNAway and RNAse Zap
{: .compact}

<div class="pagebreak"> </div>

## Protocole

### Partie 1 : Synthèse d'ADNc avec la reverse transcriptase Superscript IV

> **NOTE SUR LA PRÉPARATION DE LA CABINE :** Pour prévenir les contaminations des réactifs, cette étape doit être effectuée dans la CABINE DE PRÉPARATION DE MASTER MIX, qui est pré-stérilisée aux UV et traitée avec des lingettes, et les réactifs DNAway et RNAseZap. Nettoyer la cabine avec chacun des produits l'un après l'autre, avec 5 minutes de séchage entre passages. Les pipettes doivent aussi être traitées de la même manière, et exposées aux UV pendant 30 minutes entre chaque préparation de librairies.

1. Préparer la réaction suivante dans la cabine de master mix et ajouter 2&micro;L de réaction dans chaque tube :

    | Réactif | Volume
    |---|---
    |50&micro;M hexamères aléatoires (random hexamers) | 9&micro;L
    |10mM dNTPs mix (10mM chacun)| 9&micro;L
    |TOTAL | 18&micro;L

2. Dans la cabine d'extraction et de distribution d'échantillons, ajouter 11&micro;L d'ARN dans 7 tubes et 11&micro;L d'eau (bio-moléculaire) dans le 8ème tube qui servira de contrôle négatif.

> **NOTE :** L'ARN viral d'origine d'un échantillon clinique doit être compris entre un Ct de 18 à 35. Si le Ct est entre 12 et 15, alors diluer l'échantillon d'un facteur 100 dans l'eau ; si le Ct est entre 15 et 18, alors diluer d'un facteur 10 dans l'eau. Cette dilution réduira le risque d'une inhibition de la PCR.

3. Mélanger doucement (éviter de vortexer) puis centrifuger brièvement le tube pour assurer un contact maximum du contenu avec le thermocycleur.

4. Placer les tubes dans la machine mini16 PCR et démarrer le programme suivant (pour dénaturer l'ARN) :

    |Étape|Temperature|Temps
    |---|---|---
    | Dénaturation | 65&deg;C | 5 mins
    | Hybridation des amorces | Glace | 1 min

5. Dans la cabine de master mix, préparer le master mix de synthèse d'ADNc :

    | Réactif | Volume
    |---|---
    |Tampon (Buffer) SSIV | 36&micro;L
    |100mM DTT | 9&micro;L
    |RNaseOUT RNase Inhibitor | 9&micro;L
    |SSIV Reverse Transcriptase | 9&micro;L
    |TOTAL | 63&micro;L

6. Dans la cabine d'extraction et de distribution d'échantillons, ajouter 7&micro;L du master mix au tubes d'ARN dénaturé
7. Mélanger doucement (éviter de vortexer) puis centrifuger brièvement le tube pour assurer un contact maximum avec le thermocycleur.
8. Dans la machine mini16 PCR, incuber la réaction selon le programme suivant :

    |Étape|Temperature|Temps
    |---|---|---
    | Extension | 42&deg;C | 50 mins   
    | Inactivation | 70&deg;C | 10 mins

9. L'ADNc est maintenant prêt pour la synthèse des amplicons. Transférer les tubes d'ADNc dans la cabine d'extraction et de distribution d'échantillons.

<div class="pagebreak"> </div>

### Partie 2 : Préparation des amplicons d'Ebola

Les amorces Ebola de ce protocole ont été préparées grâce à [Primal Scheme](http://primal.zibraproject.org) et génèrent des amplicons chevauchants de 400 nt. Les noms des amorces et leurs dilutions sont listées dans le tableau suivant.

Le stock d'amorces 100nM doivent être préparées et aliquotées AVANT LE DÉPART dans la cabine de master mix.

#### Dilution des amorces à 10&micro;M et préparation du master mix de PCR

1. Diluer d'un facteur 10 le stock d'amorces 100nM dans de l'eau de grade moléculaire pour générer les stocks d'amorces à 10&micro;M (amorces de travail). Il est recommandé que plusieurs aliquots de chaque pool d'amorces soient préparés afin de tenir compte des risques de dégradation ou de contamination.

> **NOTE :** Les amorces doivent être utilisées à une concentration finale de 0.015&micro;M par amorce. Ainsi, Pool 1 contient 64 amorces : il est donc nécessaire d'ajouter 2.4&micro;L du Pool 1 à 10&micro;M pour chaque réaction de 25&micro;L. Le pool 2 contient 64 amorces : il est donc nécessaire d'ajouter 2.4&micro;L du Pool 2 à 10&micro;M pour chaque réaction de 25&micro;L. Pour d'autres approches, ajuster le volume de manière appropriée.

2. Dans la cabine de master mix, préparer les 2 master mixes pour les pool 1 et pool 2, et distribuer 22.5&micro;L de chaque mix dans les tubes pour le pool 1, puis dans les tubes pour le pool 2.

    | Réactif | Volume
    |---|---
    |Q5 reaction buffer (5×)           |45&micro;L
    |dNTPs (10 mM ea.)                 |4.5&micro;L
    |Q5 DNA polymerase                 |2.25&micro;L
    |Pool d'amorces 1 ou 2 (10&micro;M)|2.4&micro;L
    |Eau                               |129.15&micro;L
    |TOTAL                             |183.3&micro;L

3. Dans la cabine d'extraction et distribution d'échantillon, ajouter 2.5&micro;L d'ADNc à chaque tube de réaction Pool1 et Pool2 et bien mélanger en tapotant les tubes.

4. Centrifuger brièvement les tubes pour que leur contenu soit bien au fond.

5. Placer les tubes dans la machine mini16 PCR, démarrer le programme de PCR comme suit:

    |Étape                     |Temperature |Temps       |Cycles
    |--------------------------|------------|------------|-------
    |Activation par la chaleur |98&deg;C    |30 secondes |1
    |Dénaturation              |98&deg;C    |15 secondes |30
    |Hybridation               |65&deg;C    |300 secondes|30
    |Maintien                  |4&deg;C     |Indéfini    |1

> **NOTE :** Le nombre de cycle doit être de 25 pour des Ct compris entre 18 et 21 jusqu'à un maximum de 35 cycles pour Ct 35.

> **NOTE :** La machine mini16 PCR doit être connectée au "PowerAdd", qui joue le rôle d'un UPS, en cas de coupure de courant.

6. Purifier les amplicons en utilisant le protocole suivant dans la cabine de post-PCR :

    1. Centrifuger brièvement et combiner entièrement le contenu des réactions de PCR “Pool1” et “Pool2” pour chaque échantillon biologique dans un seul tube Eppendorf 1.5mL.

    2. S'assurer que les billes Ampure XP sont bien resuspendues en mélangeant vigoureusement avant d'ajouter à l'échantillon. Le mélange doit être d'une couleur brune homogène.

    3. Ajouter un volume équivalent de billes Ampure XP dans le tube et mélanger délicatement soit en pipettant ou en tapotant avec le doigt. Le volume total doit d'environ 50&micro;L, donc ajouter 50&micro;L de billes.

    4. Bien vortexer puis centrifuger brièvement les tubes pour enlever les billes du couvercle ou des parois du tube.

    5. Incuber 5 mins à température ambiante.

    6. Placer sur un support magnétique et incuber 2 minutes ou jusqu'à ce que les billes aient formé un culot contre l'aimant et que la solution soit complètement transparente.

    7. Enlever et jeter avec précaution la solution, en faisant attention de ne pas toucher le culot de billes.

    8. Ajouter 200&micro;L d'éthanol 70% à température ambiante au culot.

    9. Enlever et jeter avec précaution l'éthanol, en faisant attention de ne pas toucher le culot de billes.

    10. Répeter les étapes `h` à `i` pour laver à nouveau le culot.

    11. Centrifuger brièvement le culot et enlever avec précaution autant d'éthanol que possible en utilisant un cône de 10&micro;L.

    12. Laisser le culot sécher 1 minute, en éviter de trop le déssecher (si le culot commencer à craqueler, alors il est trop sec).

    13. Resuspendre le culot dans 31&micro;L de Tris 10mM, et incuber pour 2 mins.

    14. Placer sur un support magnétique et AVEC PRÉCAUTION enlever l'eau et la transférer dans un tube Eppendorf de 1.5mL propre. ASSUREZ-VOUS qu'aucune bille ne soit transférée dans ce tube. Dans certains cas, une brève centrifugation peut être utile pour culotter les billes résiduelles.

    15. Quantifier les mélanges d'amplicons en utilisant le protocole ONE dsDNA du fluoromètre Quantus.

<div class="pagebreak"> </div>

### Partie 3 : Quantification Quantus des mélanges d'amplicons

1. Sur la feuille de calcul de dilution, noter les identifiants des échantillons, et la concentration d'ADN mesurée. Si la concentration est supérieure à 25 ng/micro;L, diluer l'échantillon par un facteur 10 en ajoutant 270 micro;L de Tris 10mM et quantifier de nouveau en utilisant le protocole ONE dsDNA du fluoromètre Quantus.

> **NOTE :** Pour préparer du Tris 10mM, dans la cabine de master mix, ajouter 10 &micro;L de Tris 1M dans un tube Eppendorf et ajouter 990 &micro;L d'eau.

2. Préparer le nombre requis de tubes 0.5mL.

> **NOTE :** N'utiliser que des tubes PCR à paroi fine et transparente de 0.5mL.

3. Annoter le couvercle des tubes. Ne pas annoter les côtés du tube, cela pourrait interférer avec la lecture de l'échantillon.

4. Ajouter 199&micro;L de la solution "ONE dsDNA dye" à chaque tube.

5. Ajouter 1&micro;L de chaque échantillon au tube correspondant.

> **NOTE :**  Utiliser une pipette P2 pour plus de précision.

6. Mélanger chaque échantillon vigoureusement en vortexant pendant 3-5 secondes.

7. Laisser les tubes incuber à température ambiante pendant 2 minutes avant de continuer.

8. Sur l'écran d’accueil du fluoromètre Quantus, sélectionner `Protocol`, puis `ONE DNA` comme type d'analyse.

> **NOTE :** Si vous avez déjà effectué une calibration pour l'analyse sélectionnée, vous pouvez continuer, il n'y a pas besoin de faire des calibrations répétées lors de l'utilisation de la solution ONE DNA pré-diluée. **Si vous souhaitez utiliser une calibration précédente, continuez à l'étape 11**. Dans le cas contraire, continuez avec l'étape 8.

9. Ajouter 200&micro;L de solution "ONE dsDNA Dye" à deux tubes de 0.5mL.

10. Ajouter 1&micro;L d'ADN Lambda standard à 400 ng/&micro;L fourni avec le kit dans l'un des deux tubes. Ces deux tubes sont respectivement le blanc et le standard requis pour effectuer la procédure de calibration à un point.

11. Sélectionner `Calibrate`, puis `ONE DNA` et placer le blanc dans le lecteur puis sélectionner `Read Blank`. Ensuite placer le standard dans le lecteur et sélectionner `Read Std`.

12. Sur l'écran d’accueil, naviguer sur `Sample Volume` et régler sur 1&micro;L puis sur `Units` et régler sur ng/&micro;L.

13. Placer le premier échantillon dans le lecteur et fermer le couvercle. La concentration est lue automatiquement lors de sa fermeture.

14. Répéter l'étape 12 jusqu'à ce que tous les échantillons aient été lus.

15. La valeur affichée à l'écran est la concentration d'ADN double-brin. **Consigner avec soin tous les résultats** dans un tableur ou un cahier de laboratoire.

<div class="pagebreak"> </div>

### Partie 4: Barcoding et ligation des adapteurs: protocole en tube unique

> **NOTE:** Ceci est un protocole en tube unique pour la préparation de librairies avec ligation de barcode natifs. Nous n'avons observé aucune réduction de performance par rapport aux librairies standards, et peut même être plus rapide si l'on utilise le module Ultra II® ligation, qui est compatible avec le module Ultra II® end repair/dA-tailing en retirant une étape de purification. Si vous avez le temps, on recommande de doubler les temps d'incubation en <span style="color:blue">bleue</span>. Si vous êtes pressés, les temps indiqués en <span style="color:red">rouge</span> sont un bon compromis entre vitesse et efficacité.

1. Dans la cabine de mastermix, préparer la réaction de préparation d'extrémité (End Prep) suivante, et distribuer 13&micro;L dans une nouvelle barette de 8 tubes.

   | Réactif | Volume
   |---|---
   | Eau       | 94.5&micro;L
   | Ultra II End Prep Reaction Buffer | 15.75&micro;L
   | Ultra II End Prep Enzyme Mix | 6.75&micro;
   | Total     | 117&micro;L  

2. Dans la cabine de post-PCR, ajouter 2&micro;L d'amplicon (à la concentration 2.5&ng/&micro;L) dans chaque tube.

> **NOTE:** La quantité d'amplicons peut varier de 5-10ng, mais pas au-delà: le molarité de l'ADN serait trop élevée pour un barcoding efficace. Il faut avoir 6 échantillons par chaque librairie barcode natif pour avoir suffisamment de matériel à la fin.

3. Dans la machine mmini16 PCR, incuber 5 mins les tubes dans la machine éteinte, avec un pain de glace en dessous (pour mimer les 20°C nécessaires). Puis allumer la machine et lancer un programme à 65&deg;C pendant 5 mins.
Une fois le cycle terminé, transférer ces tubes dans la cabine post-PCR.

4. Placer sur glace pendant 30 secondes.

5. Dans la cabine de master mix, préparer le master mix suivant, vortexer et centrifuger brièvement :

    | Réactif | Volume
    |---|---
    | Ultra II Ligation Master Mix | 168&micro;L
    | Ligation Enhancer | 4.8&micro;L
    | Total | 172.8&micro;L

6. Distribuer 19.8 &micro;L du mix dans chaque tube d'une nouvelle barette de 8 tubes. Puis ajouter 2.75 &micro;L de barcode NBXX dans chaque tube (un barcode par tube).

7. Dans la cabine post-PCR, prendre 20.5&micro;L du master mix barcodé et ajouter aux tubes de réaction précédents (obtenu à l'étape de préparation d'extrémité).

8. Dans la machine mmini16 PCR, incuber 15 mins les tubes dans la machine éteinte, avec un pain de glace en dessous (pour mimer les 20°C nécessaires). Puis allumer la machine et lancer un programme à 70&deg;C pendant 10 mins. Placer sur la glace ensuite.

> **NOTE:** Cette étape vise à inactiver l'ADN ligase pour éviter des croisements entre barcodes.

9. Mélanger tous les fragments barcodés ensemble dans un tube Eppendorf 1.5mL propre.

10. Ajouter 284&micro;L de billes Ampure XP au tube.

11. Incuber 5 mins.

12. Placer sur un support magnétique et incuber 2 minutes ou jusqu'à transparence.

13. Enlever la solution.

14. Ajouter 200&micro;L d'éthanol à 70%, toujours sur le support magnétique.

15. Enlever et jeter l'éthanol sans toucher le culot.

16.	Répéter les étapes 13 et 15.

17.	Enlever l'éthanol 70% résiduel puis sécher à l'air libre pendant 5 min.

18.	Resuspendre dans 31&micro;L de Tris 10mM.

19.	Incuber hors du support magnétique pendant 2 minutes.

20.	Replacer sur le support magnétique.

21. Attendre que la solution devienne transparente puis transférer la solution dans un petit tube PCR 0.2ml

22.	Prendre 1&micro;L pour mesurer la concentration par Quantus comme décrit au-dessus. La concentration attendue est d'environ 1ng/&micro;L.

23. Dans la cabine de master mix, préparer la réaction de ligation d'adaptateur suivante :

    | Réactif | Volume
    |---|---
    | NEBNext Quick Ligation Reaction Buffer (5X) | 11&micro;L
    | AMII adapter mix | 5.5&micro;L
    | Quick T4 DNA Ligase | 5.5&micro;L
    | Volume total | 22&micro;L

Dans la cabine post-PCR, ajouter 20&micro;L du master mix au pool d'amplicons barcodés, puis vortexer et centrifuger brièvement.

24. Dans la machine mmini16 PCR, incuber 15 mins le tube dans la machine éteinte, avec un pain de glace en dessous (pour mimer les 20°C nécessaires).

25. Dans la cabine post-PCR, transférer le contenu du tube 0.2ml dans un tube Eppendorf 1.5mL.

26. Ajouter 50&micro;L de billes Ampure XP. Vortexer et centrifuger brièvement.

27. Incuber pendant 5 mins.

28. Placer sur un support magnétique jusqu'à transparence.

29. Retirer le surnageant.

30. Ajouter 200&micro;L de SFB et resuspendre en tapotant avec le doigt.

> **ATTENTION :** Ne pas utiliser d'éthanol à 80%.

31. Placer sur le support magnétique jusqu'à transparence.

32. Retirer le surnageant.

33. Répéter le lavage au SFB.

34. Centrifuger brièvement et retirer le SFB résiduel.

35. Ajouter 15&micro;L de tampon EB et resuspendre en tapotant avec le doigt.

36. Incuber à température ambiante pour 2 mins.

37. Placer sur le support magnétique.

38. Transférer avec précaution dans un tube Eppendorf 1.5mL propre.

39. Prendre 1&micro;L pour mesurer la concentration avec le fluoromètre Quantus comme décrit au-dessus. La concentration attendue est d'environ 1ng/&micro;L.

> **NOTE :** Les librairies peuvent être stockées à 4&deg;C si nécessaire, mais pour un meilleur résultat, il est préférable de continuer immédiatement avec le séquençage.

<div class="pagebreak"> </div>

### Partie 5 : Amorçage et chargement sur la flowcell SpotON

1. Décongeler les réactifs suivants à température ambiante avant de les placer sur glace:
   - Sequencing buffer (SQB) [tampon de séquençage]
   - Loading beads (LB) [les billes pour le chargement de la flowcell]
   - Flush buffer (FB) [tampon pour purger a flowcell]
   - Flush tether (FLT)

2. Ajouter 30&micro;L de FLT au tube de FB et bien mélanger.

3. Retourner le couvercle de la flowcell et faire glisser le couvercle du port d'amorçage au sens des aiguilles d'une montre pour que le port d’amorçage devienne visible.

> **ATTENTION :** Cette étape doit être faite avec précaution. La matrice des pores doit être constamment couverte par un tampon. Retirer plus que 20-30&micro;L risque d'endommager les pores.

4. Après avoir ouvert le port d'amorçage, vérifier s'il n'y a pas de petites bulles d'air sous le couvercle. Aspirer un petit volume pour enlever toute bulle (quelques &micro;Ls):   
   - Régler une pipette P1000 sur 200&micro;L   
   - Insérer le cône dans le port d'amorçage  
   - Tourner la molette de la pipette jusqu'à ce que le cadran indique 220-230&micro;L, ou jusqu'à ce que vous voyez un petit volume de tampon entrer dans le cône.  

5. Placer 800&micro;L du FB+FLT dans la flowcell par le port d'amorçage, utilisant la méthode décrite à l'étape 5. Éviter d’introduire des bulles d'air.

6. Attendre 5 minutes.                                            

7. Dans un nouveau tube Eppendorf propre, préparer la dilution de la librairie pour le séquençage :

    | Réactif | Volume
    |---|---
    | SQB | 37.5&micro;L
    | LB | 25.5&micro;L
    | Librairie (~10ng) | 12&micro;L
    | Total | 75&micro;L

8. Soulever doucement le couvercle du port d'échantillon SpotON pour rendre le port accessible.

9. Placer 200&micro;L du mix d'amorçage dans le port d'amorçage (***PAS*** le port d'échantillon SpotON), en évitant l'introduction de bulles d'air.

10. Mélanger doucement la librairie préparée en pipettant de haut et en bas avant de charger la flowcell.

11. Au goutte à goutte, ajouter 75&micro;L de la librairie préparée sur la flowcell par le port d'échantillon SpotON. S'assurer que chaque goutte est bien aspirée dans le port avant ajouter la goutte suivante.

12. Replacer doucement le couvercle du port d'échantillon SpotON, en s'assurant que le bouchon entre bien dans le port SpotON. Fermer le port d’amorçage et replacer le couvercle du MinION.

13. Double-cliquer sur l'icone MinKNOW sur le bureau pour ouvrir l'interface graphique MinKNOW.

14. Si votre MinION été déconnecté de l'ordinateur, le re-connecter maintenant.

15. Choisir le type de flowcell dans la boîte de sélection :

    - `FLO-MIN106` : R9.4.1 flowcell

16. Marquer la flowcell comme `Selected`.

17. Cliquer sur le bouton `New Experiment` en bas à gauche de l'interface graphique.

18. Dans l'écran popup, sélectionner les paramètres pour votre expérience dans les onglets individuels :

    - `Experiment`
    : Nommer le run dans le champ expérience, laisser le champ de l'échantillon vide.

    - `Kit`
    : Selectionner LSK109 comme il n'y a pas d'option pour le kit de barcoding natif (NBD104)

    - `Run Options`
    : Définir la durée du run de sequançage, d'ordinaire 1-2 heures.

    - `Basecalling`
    : Laisser "basecalling" allumé et vérifier que le "HAC" (high accuracy model) est selectionné.

    - `Output`
    : Le nombre de fichiers que MinKNOW écrira dans un seul dossier. Par défaut réglé sur 4000.

19. Cliquer sur `Start run`.

20. Laisser le script se dérouler jusqu'au bout.

21. La page `Experiment` du MinKNOW indiquera la progression du script ; ceci est accessible par l'onglet `Experiment` qui apparaîtra en haut à droite de l'écran.

22. Surveillez le panneau `Message` du côté droit pour les erreurs.
