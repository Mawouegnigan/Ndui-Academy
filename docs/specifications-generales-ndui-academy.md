# Spécifications générales du projet — Ndui Academy

**Certificat Développement Python — FORCE-N**
**Auteur :** *( Mawouégnigan Grégoire FANGNON)*
**Date :** Août 2026

---

## 1. Description du projet

L'accès à un enseignement biblique structuré, progressif et rigoureux reste aujourd'hui limité pour beaucoup d'apprenants à travers le monde, faute de plateformes dédiées offrant un vrai parcours pédagogique — organisé par livre, thème ou personnage biblique — avec suivi de progression et évaluation.

Face à ce constat, nous avons décidé de développer **Ndui Academy** — du mot adja *"n'dui"*, signifiant *savoir* et *intelligence* — une plateforme d'apprentissage en ligne (LMS) dédiée à l'étude biblique. Elle permettra aux apprenants de suivre des parcours structurés, de progresser leçon après leçon, de s'évaluer via des QCM corrigés automatiquement, et de participer à des challenges communautaires (réponses audio, vidéo ou texte) avec classement public.

L'architecture de la plateforme est pensée dès sa conception pour être **générique et extensible** : au-delà de l'étude biblique, elle pourra à terme accueillir d'autres domaines d'étude, sans refonte technique majeure.

Ce projet vise à démontrer une version fonctionnelle et sécurisée de la plateforme, en vue d'un déploiement à grande échelle capable de servir des milliers d'utilisateurs à travers le monde, avec un premier lancement ciblé sur le **Bénin**.

---

## 2. QQOQCP

| Question | Réponse |
|---|---|
| **Qui ?** | Apprenants souhaitant étudier la Bible de façon structurée ; administrateur gérant les contenus pédagogiques |
| **Quoi ?** | Une plateforme LMS (Learning Management System) dédiée à l'étude biblique : parcours, leçons, évaluations, challenges communautaires, certification |
| **Où ?** | Plateforme web accessible internationalement, avec un premier lancement ciblé sur le Bénin |
| **Quand ?** | Mise en production prévue à l'issue du projet |
| **Comment ?** | Développement d'une application web avec back-end Python/Django, base de données PostgreSQL, front-end Angular, sécurisation complète (CSRF, sessions, anti-bruteforce, validation des fichiers) |
| **Pourquoi ?** | Démocratiser l'accès à un enseignement biblique structuré et rigoureux, à l'échelle mondiale |

---

## 3. Analyse SWOT

| | **Positif** | **Négatif** |
|---|---|---|
| **Interne** | **Forces (Strengths)**<br>• Cahier des charges fonctionnel déjà bien maîtrisé (parcours, leçons, évaluations, challenges) grâce à une expérience concrète du domaine<br>• Stack technique moderne et robuste (Django, Angular, PostgreSQL) adaptée à la montée en charge<br>• Fonctionnalités différenciantes : challenges communautaires multi-format (audio/vidéo/texte) avec classement public<br>• Vision claire de la sécurité dès la conception<br>• Architecture pensée dès le départ pour être extensible à d'autres domaines d'étude | **Faiblesses (Weaknesses)**<br>• Développeur unique : capacité de développement limitée, dépendance forte à une seule personne<br>• Délai de réalisation contraint par le calendrier de la formation<br>• Pas encore d'expérience de déploiement à très grande échelle<br>• Module de certification prévu en conception mais non disponible dès le lancement |
| **Externe** | **Opportunités (Opportunities)**<br>• Marché de l'e-learning en forte croissance, notamment pour les contenus éducatifs/religieux de niche<br>• Peu de plateformes dédiées spécifiquement à l'étude biblique structurée avec suivi de progression et certification<br>• Lancement ciblé sur le Bénin en premier marché : ancrage local facilitant les retours utilisateurs, partenariats et tests avant extension internationale<br>• Public cible mondial à terme, propice à l'effet réseau (partage, classements)<br>• Possibilité de partenariats avec des organisations religieuses/éducatives locales puis internationales<br>• Modèle extensible à d'autres types de formations à terme | **Menaces (Threats)**<br>• Concurrence de plateformes LMS génériques réutilisables pour du contenu religieux<br>• Dépendance à la modération humaine pour les réponses non automatisables, limitant la scalabilité<br>• Sensibilité du sujet (contenu religieux) nécessitant vigilance sur la neutralité selon les marchés visés<br>• Évolution rapide des standards de sécurité web<br>• Risque de charge de travail élevée pour un développeur seul |

---

## 4. Besoins fonctionnels

### a. Gestion Onboarding
- Visualisation publique des domaines d'étude et parcours disponibles (nom, description, durée, prérequis)
- Inscription via formulaire ou compte Google/Facebook (OAuth)
- Un apprenant peut s'inscrire à plusieurs parcours

### b. Gestion du profil apprenant
- Modification des informations (nom, prénom, date de naissance...)
- Changement de mot de passe
- Vérification de l'email

### c. Gestion des domaines d'étude et parcours *(cœur générique de la plateforme)*
- Un **domaine d'étude** (ex : "Étude biblique") regroupe plusieurs **parcours**
- Un **parcours** regroupe plusieurs **cours**
- Un **cours** regroupe : leçons, ressources, évaluations (QCM)
- Progression séquentielle : déblocage d'une leçon après validation de la précédente
- Interface administrateur pour créer et gérer domaines, parcours, cours, leçons

### d. Évaluations et Challenges
- QCM avec correction automatique et suivi de score
- Challenges communautaires (réponses audio, vidéo, texte libre)
- Classement public par challenge/parcours
- Correction manuelle par l'admin pour les réponses non automatisables

### e. Certification
- Génération **automatique** d'un certificat (PDF) à la fin d'un parcours, si le score minimum requis est atteint
- Format du numéro de certificat : `CA-{année}-BJ-{numéro d'ordre}`
- QR code de vérification sur chaque certificat, renvoyant vers une page publique de validation
- Certificat téléchargeable/consultable depuis le profil de l'apprenant

### f. Dashboard Apprenant
- Statistiques de progression par parcours
- Historique des challenges : participations, résultats, statut de correction (auto/manuelle en attente)
- Classement (leaderboard) : rang de l'apprenant, points/score, comparaison avec les autres apprenants
- Système de points/gamification : points gagnés par leçon terminée, quiz réussi, challenge complété — avec badges/récompenses débloquées
- Espace mentorat : mise en relation avec un mentor, suivi des échanges
- Espace de dépôt de projet : zone dédiée pour soumettre un mini-projet ou une production liée à un parcours
- Webinaires : liste des webinaires à venir + accès aux enregistrements passés
- Chat **temps réel** par parcours : messagerie réservée aux apprenants inscrits à un même parcours
- Certificats obtenus : liste avec numéro, date, QR code, lien de vérification publique

### g. Administrateur
- Gestion des domaines d'étude, parcours, cours, leçons
- Gestion des comptes utilisateurs
- Correction manuelle des challenges
- Suivi des certifications délivrées

---

## 5. Besoins techniques

### a. Stack technique

| Composant | Technologie | Justification |
|---|---|---|
| Backend | Django (+ Django REST Framework) | Framework robuste, sécurisé par défaut, ORM puissant |
| Temps réel (chat) | Django Channels + Redis | Gestion des WebSockets pour le chat par parcours |
| Serveur applicatif | Daphne / Uvicorn (ASGI) | Support de Channels en plus du WSGI classique |
| Frontend | Angular (TypeScript) | Conforme au référentiel Force-N, structuré pour une application d'entreprise |
| Base de données | PostgreSQL | Fiable, performante, bien intégrée à Django |
| Stockage fichiers | Stockage objet compatible S3 (ou disque + CDN à terme) | Fichiers jusqu'à 100 Mo (challenges audio/vidéo) |
| Génération PDF | WeasyPrint / ReportLab | Génération automatique des certificats |
| QR Code | Librairie Python `qrcode` | Génération du QR de vérification |
| Authentification | Django auth + OAuth 2.0 (Google, Facebook) | Inscription simplifiée |

### b. Sécurité
- Protection des fichiers de configuration et secrets techniques (variables d'environnement)
- Externalisation des identifiants sensibles
- Protection CSRF (native Django)
- Sécurisation des sessions utilisateurs
- Protection contre les attaques par force brute
- Validation stricte des fichiers envoyés
- Connexions chiffrées en HTTPS
- Authentification OAuth sécurisée

### c. Performance
- Temps de chargement cible : inférieur à 3 secondes
- Support visé : plusieurs milliers d'utilisateurs simultanés
- Architecture pensée pour la montée en charge horizontale

### d. Compatibilité
- Application web responsive (ordinateur et mobile via navigateur)
- Compatibilité iOS et Android via le web responsive dans un premier temps

### e. Accessibilité
- Respect des normes WCAG 2.1

### f. Architecture évolutive
- Modèle de données générique (Domaine d'étude → Parcours → Cours → Leçons)
- Architecture facilitant l'ajout de nouveaux modules à terme

---

## 6. Design et expérience utilisateur

Interface utilisateur (UI)

Interface moderne, sobre et épurée, favorisant la lisibilité des contenus d'étude
Palette de couleurs et identité visuelle propres à Ndui Academy, cohérentes avec la charte graphique Force-N pour les livrables du certificat
Design responsive (adaptation fluide web/mobile)
Mise en avant visuelle de la progression (barres de progression, badges, statut des leçons débloquées/verrouillées).

Expérience utilisateur (UX)

Parcours d'inscription simplifié (formulaire ou OAuth Google/Facebook en un minimum de clics)
Navigation intuitive entre domaines d'étude, parcours, cours et leçons
Accès rapide au dashboard, aux challenges et au classement depuis un menu principal clair
Feedback immédiat lors des évaluations (résultat du QCM affiché instantanément)
Notifications pour informer l'apprenant d'un nouveau message (chat parcours), d'une correction manuelle effectuée, ou d'un certificat obtenu.

## 7. Planning et livrables

*(à venir)*
