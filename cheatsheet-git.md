# Petit pense-bête pour GIT
## Rien de très avancé

Explication de [git](https://git-scm.com/book/en/v1/) en ligne.

### Initialisation pour le fork
``` bash
# Appuyer sur le bouton fork depuis https://github.com/ruthrapr/documents-structures
# Dans un terminal
git clone https://github.com/VOTRE-NOM-UTILISATEUR/documents-structures

git remote add upstream https://github.com/ruthrapr/documents-structures
```

### Pour récupérer les update
```bash
# Depuis votre dossier en local
git fetch upstream
git checkout master
git merge upstream/master
``` 
Si tout a fonctionné, les mises à jours devraient être rappatriées.

### Initialiser un repository git
```bash
# Depuis un dossier local
cd mon-projet
git init .

# Depuis un repository distant
git clone url
```

### Vérification du repository
```bash
git status
```

### Ajout d'un fichier
```bash
echo "Hello" > mon-fichier.txt

# Optionnel mais permet de voir les changements
git status

git add mon-fichier.txt
```

### Supprimer ou déplacer un fichier
```bash
git rm mon-fichier.txt
git mv mon-fichier.txt
```

### Faire un commit
```bash
git commit -m "mon message"
```

### Rapatrier les derniers changements
```bash
git pull
```

### _Pusher_ les changements
```bash
git push
```

### Créer et changer de branche
```bash
git checkout -b ma-branche
```

### Changer de branche
```bash
git checkout ma-branche
```

### Supprimer ma branche
```bash
git branch -d ma-branche
```

### Rapatrier ses changements sur une autre branche
```bash
git checkout branche-où-on-veut-rapatrier
git merge branche-a-rapatrier
```
