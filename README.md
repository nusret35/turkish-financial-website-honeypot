# Turkish Financial News Website Honeypot

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Best decoy to trick attackers and monitor their actions.**



# Description

This project initially created for Cybersecurity Applications course which turned out as a good, useful, easy-to-use decoy. The repository includes a financial website template. The feed is fetched from an RSS. Here is the [link](https://www.ekonomidunya.com/rss_ekonomi_1.xml ) for it. The project consists of Flask backend with pure HTML frontend. MySQL is used for the database. The vulnerabilities include stored and reflected XSS, SQL Injection, cryptographic failure (MD5 used for hashes) and unvalidated redirect. The vulnerabilities and their locations are indicated below. Also, all the database tables and sample data content are specified as well. Every action of the attacker is logged to the ```app.log``` file.


## Main Page
<img width="1000" alt="ss-honey" src="https://github.com/nusret35/turkish-financial-website-honeypot/assets/96892300/90306b72-1158-4d08-9e83-4c6f285abff5">

## Search Result Page
<img width="1000" alt="ss-honey2" src="https://github.com/nusret35/turkish-financial-website-honeypot/assets/96892300/5f0abcae-a868-4794-af19-5cbdb1f80785">

## Login Page
<img width="1000" alt="ss-honey3" src="https://github.com/nusret35/turkish-financial-website-honeypot/assets/96892300/02005334-ef7d-48e1-a858-5945a8de78eb">

# Prerequisites

In order to run the project, you should have installed the packages in that are indicated in the requirements.txt. You can just run the following command (inside the directory) to download all the packages:

```bash
pip install -r requirements.txt
```

Create all the necessary database tables. They are specified below.

Finally, just run ```main.py``` and you are good to go:

```bash
python3 main.py
```

# Contributors

The developers of this project are [Nusret Ali Kızılaslan](https://github.com/nusret35), [Ali Vehbi Güneysu](https://github.com/alivehbi), and [Uğur Yüce](https://github.com/yuceugur). If you have any further questions, don't hesitate to contact us. We are open for pull requests and any further development.

# Database Tables

First, create the database ```turkishdb```:

```sql
CREATE DATABASE turkishdb;
```

## Users Table

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(255) DEFAULT 'user'
);
```
## Comments Table



```sql
CREATE TABLE comments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    news_link VARCHAR(255) NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
);


```
## Coins Table

```sql
CREATE TABLE coins (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255));

```
## TrackAd Table

```sql
CREATE TABLE TRACKAD (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user VARCHAR(255),
    date DATETIME,
    url VARCHAR(255)
);

```
## Economists Table

```sql
CREATE TABLE economists (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),image_url VARCHAR(255),short_info TEXT);
```


# Vulnerabilities

## SQL Injection

### Insert these commands to search fields in '/coins' and '/economists' pages

```sql
';INSERT INTO coins (name, url) values ('btc','btc.org');--
```

```sql
';DROP TABLE coins;--
```


## Reflected XSS

### Insert this HTML command to keyword search field

```html
<img src=1 onerror="alert('hacked')"/>
```

## Stored XSS

### Insert this HTML command to comment

```html
<script>alert('hacked')</script>
```


# Data

## Coins

```sql
INSERT INTO coins (name, url) VALUES 
('bitcoin','bitcoin.org'),
('ethereum', 'ethereum.com'), 
('ripple', 'ripple.com'),
('mina','mina.com'),
('litecoin', 'litecoin.com'),
('cardano', 'cardano.com'),
('tezos', 'tezos.com'),
('tron', 'tron.com'),
('cosmos', 'cosmos.com'),
('vechain', 'vechain.com'),
('eos', 'eos.com'),
('iota', 'iota.com'),
('neo', 'neo.com'),
('dash', 'dash.com'),
('zcash', 'zcash.com'),
('nem', 'nem.com'),
('stellar', 'stellar.com'),
('chainlink', 'chainlink.com'),
('monero', 'monero.com'),
('maker', 'maker.com'),
('uniswap', 'uniswap.com'),
('aave', 'aave.com'),
('compound', 'compound.com'),
('synthetix', 'synthetix.com'),
('yearn.finance', 'yearn.finance.com'),
('algorand', 'algorand.com'),
('filecoin', 'filecoin.com'),
('sushiswap', 'sushiswap.com'),
('polygon', 'polygon.com'),
('solana', 'solana.com'),
('avalanche', 'avalanche.com'),
('terra', 'terra.com'),
('hedera', 'hedera.com'),
('elrond', 'elrond.com'),
('decred', 'decred.com'),
('harmony', 'harmony.com'),
('celo', 'celo.com'),
('horizen', 'horizen.com'),
('curve DAO Token', 'curve.com'),
('0x', '0x.com'),
('ontology', 'ontology.com'),
('loopring', 'loopring.com'),
('icon', 'icon.com'),
('kyber network', 'kyber.com'),
('ren', 'ren.com'),
('balancer', 'balancer.com'),
('band protocol', 'band.com'),
('omg network', 'omg.com'),
('reserve rights', 'reserve.com'),
('ampleforth', 'ampleforth.com'),
('kusama', 'kusama.com'),
('thorchain', 'thorchain.com'),
('serum', 'serum.com'),
('the graph', 'thegraph.com'),
('arweave', 'arweave.com'),
('pancakeswap', 'pancakeswap.com'),
('safemoon', 'safemoon.com'),
('shiba inu', 'shibainu.com'),
('dogelon mars', 'dogelonmars.com'),
('baby doge coin', 'babydoge.com'),
('feg token', 'fegtoken.com'),
('akita inu', 'akitainu.com'),
('kuma inu', 'kumainu.com'),
('pig finance', 'pigfinance.com'),
('hokkaidu inu', 'hokkaiduinu.com'),
('kishu inu', 'kishuinu.com'),
('samoyedcoin', 'samoyedcoin.com'),
('mini doge', 'minidoge.com'),
('doge killer', 'dogekiller.com'),
('dogebonk', 'dogebonk.com'),
('dogedash', 'dogedash.com'),
('floki inu', 'flokiinu.com'),
('dogecoin 2.0', 'dogecoin2.com'),
('doge gf', 'dogegf.com'),
('woofy', 'woofy.com'),
('karencoin', 'karencoin.com'),
('husky', 'husky.com'),
('doggy', 'doggy.com'),
('dogira', 'dogira.com'),
('dogezilla', 'dogezilla.com'),
('catbonk', 'catbonk.com'),
('catgirl', 'catgirl.com'),
('nekocoin', 'nekocoin.com'),
('tiger king', 'tigerking.com'),
('lion token', 'liontoken.com'),
('panther swap', 'pantherswap.com'),
('leopard', 'leopard.com'),
('cheetah token', 'cheetahtoken.com'),
('jaguar swap', 'jaguarswap.com'),
('puma pay', 'pumapay.com'),
('fox finance', 'foxfinance.com'),
('wolf safe poor people', 'wolfsafepoorpeople.com'),
('bear token', 'beartoken.com'),
('bull token', 'bulltoken.com'),
('eagle token', 'eagletoken.com'),
('falcon swap', 'falconswap.com'),
('hawk token', 'hawktoken.com'),
('owl token', 'owltoken.com'),
('sparrow token', 'sparrowtoken.com'),
('dove token', 'dovetoken.com');
('milancoin','milan-coin.com'),
('bnb','bnb-coin.com') ;
```

## Users

``` sql
INSERT INTO users (username,password) VALUES 
("ugur", "pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd"), 
("alivehbi", "pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd"), 
("nusret", "pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd"), 
("ekonomist", "pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd"), 
("ozgur celiktas", "pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd"), 
('aaron94', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('ashley38', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('josesmith', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('williamskenneth', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('james54', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('tonya92', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('shannon65', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('xjones', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('bvillanueva', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('trevorarnold', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('johnwatson', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('jeffreydavis', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('garzamarcus', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('cindy29', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('david40', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('dominiquesimpson', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('richardhunt', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('maryphillips', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('ohopkins', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('mhart', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('ydixon', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('jhoward', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('nblair', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('tford', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('lbrown', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('franklinelizabeth', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('vdawson', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('hineschristy', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('stephaniecarter', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('galexander', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('mcooper', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('leonmichael', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('timothy91', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('sherrysnow', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('ronaldanderson', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('rsaunders', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('shelly83', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('danielnguyen', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('daniel65', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('vmccormick', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('david58', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('destinyhill', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('pjordan', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('anthony27', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('garcianicholas', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('penabenjamin', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('tyler22', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('muellersarah', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('pnolan', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('bchang', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('william00', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('kylie53', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('ryandaniel', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('danielgoodwin', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('clowery', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('darrellgutierrez', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('ritterjessica', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('martinezrhonda', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('annamartinez', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('ilyons', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('derek01', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('anthony99', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('kayla12', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('jthompson', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('harrisamber', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('morgancox', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('lgonzalez', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('wclay', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('lpruitt', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('cortezcaitlyn', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('michael61', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('larry46', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('eduardobrown', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('christopherwinters', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('scott26', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('jacquelineskinner', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('matthew16', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('allisonbell', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('gibsonkent', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('thompsontheresa', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('brooksjessica', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('edwarddouglas', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('gerald37', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('johnsonrobin', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('antoniohill', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('jennifer55', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('wpreston', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('thomaszhang', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('imichael', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('fergusondouglas', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('riversrichard', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('jason22', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('jennifer58', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('jackson74', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('nina37', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('kyle14', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('jonesdonna', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('colenathan', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('opowell', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd') ,
('millersandra', 'pbkdf2:md5:600000$ILSRaY79USIMO5ra$bbce65e515f7576ea83cb94621e18edd');
```

## Economists

``` sql
INSERT INTO economists (name, image_url, short_info) VALUES ('Paul Rogers', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Amanda Hill', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Deborah Stewart', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Robert Schultz', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Sarah Crawford', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Christopher Martin', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Katelyn Little', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Gary Sandoval', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Jeremy Bauer', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Jon Mcbride', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Rebecca Evans', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Colleen Hull', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Kathleen Wilson', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Emily White', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Chelsea Booker', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Susan Fuller', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Travis Harris', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Kelly Anderson', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Michael Carter', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Daniel Levine', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Nathaniel Ortiz', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Timothy Lin', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Rachel Schaefer', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Alan Lyons', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Troy Edwards', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Alexis Clements', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Albert Tapia', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Anthony Mccormick', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Jason Fernandez', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Joshua Harris', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('April Greene', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Joshua Jones', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Marissa Ryan', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Carol Mcdonald', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Colleen Campbell', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Michael Ramos', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Brittany Roy', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Kelsey Vincent', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Jonathan Miller', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Albert Carlson', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Andrew Lawrence', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Elizabeth Young', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Nathan Smith', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Amanda Chen', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Deanna Raymond', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Ashley Floyd', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Joel Roberson', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Harry Garcia', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('David Butler', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Catherine Gonzales', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Eric Smith', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Larry Ramos', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Maria Cobb', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Deanna Stewart', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Michael Sanders', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Chad Benton', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Kenneth Hull', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Christopher King', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Scott White', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Nancy Gutierrez', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Sarah Lopez', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('John Baker', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Anthony Leon', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Michael Moss', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Edwin Tucker', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Angela Heath', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Shawn Kelly', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('John Harper', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Lawrence Smith', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Julian Watkins', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Lori Garcia', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Sarah Cruz', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Christopher Taylor', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Kristy Cooper', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Nicholas Dodson', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Donna Chavez', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Julie Luna', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Jack Miller', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('David Cisneros', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Herbert Waters', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('William Jones', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Tracy Barnes', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Chad Ruiz', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Jessica Duncan', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Adam Neal', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Brian Stevenson', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Justin Maldonado', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Michele Hernandez', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Brian Mcconnell', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Diana Brewer', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Maurice Kim', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Brenda Levy', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Joshua Garcia', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Lisa Burch', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Lindsey Griffith', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Laurie Johnson', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Shane Brown', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Linda Price', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Robert Mckay', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world') ,
('Erin Garcia', 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png', 'One of the best economists in the world');
```


## TRACKAD data
``` sql
INSERT INTO TRACKAD (user,date, url) VALUES ('olnuqiy', '2024-01-04 23:25:57', 'https://www.eye-tech.co.uk'),
('mnnsl90', '2024-01-06 13:42:30', 'https://www.eye-tech.co.uk'),
('pfajg83', '2024-01-02 14:49:11', 'https://www.eye-tech.co.uk'),
('gucawulz21', '2024-01-06 18:25:17', 'https://www.eye-tech.co.uk'),
('ooveiagp', '2024-01-01 19:35:46', 'https://www.eye-tech.co.uk'),
('zkbubn', '2024-01-03 11:28:08', 'https://www.eye-tech.co.uk'),
('qkxjo', '2024-01-05 06:14:53', 'https://www.eye-tech.co.uk'),
('dxigas', '2024-01-06 04:10:22', 'https://www.eye-tech.co.uk'),
('nqjbim47', '2024-01-01 22:06:39', 'https://www.eye-tech.co.uk'),
('ivsukyj', '2024-01-02 03:18:24', 'https://www.eye-tech.co.uk'),
('wzfojv', '2024-01-05 12:57:19', 'https://www.eye-tech.co.uk'),
('xpubqt49', '2024-01-03 17:34:06', 'https://www.eye-tech.co.uk'),
('zjgbu', '2024-01-04 08:19:45', 'https://www.eye-tech.co.uk'),
('ldxmc', '2024-01-06 20:50:33', 'https://www.eye-tech.co.uk'),
('kxigl', '2024-01-01 10:22:14', 'https://www.eye-tech.co.uk'),
('jriyc', '2024-01-02 16:03:57', 'https://www.eye-tech.co.uk'),
('qzflh', '2024-01-05 23:46:02', 'https://www.eye-tech.co.uk'),
('ejoirz', '2024-01-03 05:30:29', 'https://www.eye-tech.co.uk'),
('bcaumf', '2024-01-04 14:08:41', 'https://www.eye-tech.co.uk'),
('yqgbk', '2024-01-06 09:17:15', 'https://www.eye-tech.co.uk'),
('pfjxr', '2024-01-01 18:04:52', 'https://www.eye-tech.co.uk'),
('ouytr', '2024-01-02 21:59:33', 'https://www.eye-tech.co.uk'),
('wsklv', '2024-01-05 15:38:07', 'https://www.eye-tech.co.uk'),
('bivhr', '2024-01-03 02:11:20', 'https://www.eye-tech.co.uk'),
('nlzxy53', '2024-01-04 19:27:54', 'https://www.eye-tech.co.uk'),
('yjxip78', '2024-01-06 12:15:39', 'https://www.eye-tech.co.uk'),
('mgipw', '2024-01-01 07:42:28', 'https://www.eye-tech.co.uk'),
('fzqkx', '2024-01-02 13:20:05', 'https://www.eye-tech.co.uk'),
('uqjbr', '2024-01-05 22:33:16', 'https://www.eye-tech.co.uk'),
('xowjb', '2024-01-03 16:08:42', 'https://www.eye-tech.co.uk');
('bcaumf', '2024-01-04 14:08:41', 'https://www.eye-tech.co.uk'),
('yqgbk', '2024-01-06 09:17:15', 'https://www.eye-tech.co.uk'),
('pfjxr', '2024-01-01 18:04:52', 'https://www.eye-tech.co.uk'),
('ouytr', '2024-01-02 21:59:33', 'https://www.eye-tech.co.uk'),
('wsklv', '2024-01-05 15:38:07', 'https://www.eye-tech.co.uk'),
('bivhr', '2024-01-03 02:11:20', 'https://www.eye-tech.co.uk'),
('nlzxy53', '2024-01-04 19:27:54', 'https://www.eye-tech.co.uk'),
('yjxip78', '2024-01-06 12:15:39', 'https://www.eye-tech.co.uk'),
('mgipw', '2024-01-01 07:42:28', 'https://www.eye-tech.co.uk'),
('fzqkx', '2024-01-02 13:20:05', 'https://www.eye-tech.co.uk'),
('uqjbr', '2024-01-05 22:33:16', 'https://www.eye-tech.co.uk'),
('xowjb', '2024-01-03 16:08:42', 'https://www.eye-tech.co.uk');
('bcaumf', '2024-01-04 14:08:41', 'https://www.eye-tech.co.uk'),
('yqgbk', '2024-01-06 09:17:15', 'https://www.eye-tech.co.uk'),
('pfjxr', '2024-01-01 18:04:52', 'https://www.eye-tech.co.uk'),
('ouytr', '2024-01-02 21:59:33', 'https://www.eye-tech.co.uk'),
('wsklv', '2024-01-05 15:38:07', 'https://www.eye-tech.co.uk'),
('bivhr', '2024-01-03 02:11:20', 'https://www.eye-tech.co.uk'),
('nlzxy53', '2024-01-04 19:27:54', 'https://www.eye-tech.co.uk'),
('yjxip78', '2024-01-06 12:15:39', 'https://www.eye-tech.co.uk'),
('mgipw', '2024-01-01 07:42:28', 'https://www.eye-tech.co.uk'),
('fzqkx', '2024-01-02 13:20:05', 'https://www.eye-tech.co.uk'),
('uqjbr', '2024-01-05 22:33:16', 'https://www.eye-tech.co.uk'),
('xowjb', '2024-01-03 16:08:42', 'https://www.eye-tech.co.uk');
('bcaumf', '2024-01-04 14:08:41', 'https://www.eye-tech.co.uk'),
('yqgbk', '2024-01-06 09:17:15', 'https://www.eye-tech.co.uk'),
('pfjxr', '2024-01-01 18:04:52', 'https://www.eye-tech.co.uk'),
('ouytr', '2024-01-02 21:59:33', 'https://www.eye-tech.co.uk'),
('wsklv', '2024-01-05 15:38:07', 'https://www.eye-tech.co.uk'),
('bivhr', '2024-01-03 02:11:20', 'https://www.eye-tech.co.uk'),
('nlzxy53', '2024-01-04 19:27:54', 'https://www.eye-tech.co.uk'),
('yjxip78', '2024-01-06 12:15:39', 'https://www.eye-tech.co.uk'),
('mgipw', '2024-01-01 07:42:28', 'https://www.eye-tech.co.uk'),
('fzqkx', '2024-01-02 13:20:05', 'https://www.eye-tech.co.uk'),
('uqjbr', '2024-01-05 22:33:16', 'https://www.eye-tech.co.uk'),
('xowjb', '2024-01-03 16:08:42', 'https://www.eye-tech.co.uk');
('bcaumf', '2024-01-04 14:08:41', 'https://www.eye-tech.co.uk'),
('yqgbk', '2024-01-06 09:17:15', 'https://www.eye-tech.co.uk'),
('pfjxr', '2024-01-01 18:04:52', 'https://www.eye-tech.co.uk'),
('ouytr', '2024-01-02 21:59:33', 'https://www.eye-tech.co.uk'),
('wsklv', '2024-01-05 15:38:07', 'https://www.eye-tech.co.uk'),
('bivhr', '2024-01-03 02:11:20', 'https://www.eye-tech.co.uk'),
('nlzxy53', '2024-01-04 19:27:54', 'https://www.eye-tech.co.uk'),
('yjxip78', '2024-01-06 12:15:39', 'https://www.eye-tech.co.uk'),
('mgipw', '2024-01-01 07:42:28', 'https://www.eye-tech.co.uk'),
('fzqkx', '2024-01-02 13:20:05', 'https://www.eye-tech.co.uk'),
('uqjbr', '2024-01-05 22:33:16', 'https://www.eye-tech.co.uk'),
('xowjb', '2024-01-03 16:08:42', 'https://www.eye-tech.co.uk');
```

## Comments
``` sql
INSERT INTO comments (username, content, created_at, news_link) VALUES ('alivehbi', 'bu iyi haber işte!', '2024-01-07 19:00:34', '/single.html/Borsanın 10 yıllık ocak performansı'),
('nusretk', 'ben böyle işi ya!', '2024-01-07 18:57:01', "/single.html/New York borsası ABD'nin istihdam verilerinin ardından ya") ,
('scott26', 'ah be abi!', '2024-01-07 19:00:34', '/single.html/Yatırımcı rehberi (1)') ,
('alivehbi', 'ah be abi!', '2024-01-07 18:56:03', '/single.html/Ponzi şeması hakkında merak edilenler') ,
('nusretk', 'bu iyi haber işte!', '2024-01-07 19:00:34', '/single.html/ISO; enerji depolama standartlarını Çin’de belirleyecek') ,
('ugur', 'çok saçma', '2024-01-07 18:56:45', '/single.html/Borsanın 10 yıllık ocak performansı') ,
('ugur', 'olamaz', '2024-01-07 18:56:45', '/single.html/Ticaret Bakanlığı, mevzuata aykırı davranan 58 e-ticaret') ,
('nusretk', 'ben böyle işi ya!', '2024-01-07 18:56:45', '/single.html/Türkiye İMSAD Aylık Sektör Raporu açıklandı') ,
('david58', 'milleti kandırmayı bırakın!', '2024-01-07 19:00:34', '/single.html/Ponzi şeması hakkında merak edilenler') ,
('ugur', 'ben böyle işi ya!', '2024-01-07 18:57:01', "/single.html/Kültür ve Turizm Bakanlığınca 2023'te 400 milyondan fazla") ,
('ugur', 'beğendim bu haberi', '2024-01-07 18:57:01', '/single.html/ISO; enerji depolama standartlarını Çin’de belirleyecek') ,
('scott26', 'ben böyle işi ya!', '2024-01-07 19:00:34', "/single.html/Kültür ve Turizm Bakanlığınca 2023'te 400 milyondan fazla") ,
('nusretk', 'bu iyi haber işte!', '2024-01-07 18:56:45', '/single.html/ISO; enerji depolama standartlarını Çin’de belirleyecek') ,
('alivehbi', 'çok saçma', '2024-01-07 19:00:51', '/single.html/BIST 100 endeksi, günü yüzde 1,07 değer kazanarak 7.628,7') ,
('alivehbi', 'bu performansla olacak iş değil', '2024-01-07 18:56:28', '/single.html/Yatırımcı rehberi (1)') ,
('nusretk', 'son gün için fena değil!', '2024-01-07 19:00:51', '/single.html/Borsanın 10 yıllık ocak performansı') ,
('alivehbi', 'ben böyle işi ya!', '2024-01-07 18:56:09', '/single.html/Ponzi şeması hakkında merak edilenler') ,
('alivehbi', 'bu performansla olacak iş değil', '2024-01-07 18:56:28', '/single.html/Ponzi şeması hakkında merak edilenler') ,
('scott26', 'ben böyle işi ya!', '2024-01-07 19:00:51', '/single.html/Ticaret Bakanlığı, mevzuata aykırı davranan 58 e-ticaret') ,
('david58', 'bu iyi haber işte!', '2024-01-07 18:56:03', '/single.html/Türkiye İMSAD Aylık Sektör Raporu açıklandı') ,
('ugur', 'bu performansla olacak iş değil', '2024-01-07 18:57:01', '/single.html/BIST 100 endeksi, günü yüzde 1,07 değer kazanarak 7.628,7') ,
('scott26', 'olamaz', '2024-01-07 18:56:03', '/single.html/Ticaret Bakanlığı, mevzuata aykırı davranan 58 e-ticaret') ,
('scott26', 'ben böyle işi ya!', '2024-01-07 18:57:01', '/single.html/Borsanın 10 yıllık ocak performansı') ,
('david58', 'milleti kandırmayı bırakın!', '2024-01-07 19:00:34', '/single.html/Ticaret Bakanlığı, mevzuata aykırı davranan 58 e-ticaret') ,
('david58', 'ben böyle işi ya!', '2024-01-07 18:56:28', '/single.html/BIST 100 endeksi, günü yüzde 1,07 değer kazanarak 7.628,7') ,
('ugur', 'son gün için fena değil!', '2024-01-07 18:56:45', '/single.html/ISO; enerji depolama standartlarını Çin’de belirleyecek') ,
('ugur', 'çok saçma', '2024-01-07 18:56:09', "/single.html/Kültür ve Turizm Bakanlığınca 2023'te 400 milyondan fazla") ,
('nusretk', 'bu performansla olacak iş değil', '2024-01-07 18:56:45', '/single.html/ISO; enerji depolama standartlarını Çin’de belirleyecek') ,
('ugur', 'ah be abi!', '2024-01-07 18:57:01', '/single.html/ISO; enerji depolama standartlarını Çin’de belirleyecek') ,
('nusretk', 'ah be abi!', '2024-01-07 18:57:01', '/single.html/Ponzi şeması hakkında merak edilenler') ,
('david58', 'ah be abi!', '2024-01-07 18:56:45', '/single.html/ISO; enerji depolama standartlarını Çin’de belirleyecek') ,
('nusretk', 'ben böyle işi ya!', '2024-01-07 18:57:01', '/single.html/Piyasalarda gün sonu') ,
('david58', 'ah be abi!', '2024-01-07 18:56:28', '/single.html/Yatırımcı rehberi (1)') ,
('alivehbi', 'çok saçma', '2024-01-07 18:56:28', '/single.html/ISO; enerji depolama standartlarını Çin’de belirleyecek') ,
('scott26', 'ah be abi!', '2024-01-07 18:57:01', '/single.html/ISO; enerji depolama standartlarını Çin’de belirleyecek') ,
('nusretk', 'bu iyi haber işte!', '2024-01-07 19:00:34', '/single.html/Borsanın 10 yıllık ocak performansı') ,
('david58', 'ah be abi!', '2024-01-07 18:56:28', "/single.html/Kültür ve Turizm Bakanlığınca 2023'te 400 milyondan fazla") ,
('alivehbi', 'ah be abi!', '2024-01-07 18:56:09', '/single.html/Ticaret Bakanlığı, mevzuata aykırı davranan 58 e-ticaret') ,
('scott26', 'çok saçma', '2024-01-07 19:00:34', '/single.html/Ponzi şeması hakkında merak edilenler') ,
('nusretk', 'beğendim bu haberi', '2024-01-07 18:57:01', "/single.html/New York borsası ABD'nin istihdam verilerinin ardından ya") ,
('ugur', 'çok saçma', '2024-01-07 19:00:34', "/single.html/New York borsası ABD'nin istihdam verilerinin ardından ya") ,
('scott26', 'bu performansla olacak iş değil', '2024-01-07 18:57:01', '/single.html/Türkiye İMSAD Aylık Sektör Raporu açıklandı') ,
('nusretk', 'bu performansla olacak iş değil', '2024-01-07 19:00:51', '/single.html/Piyasalarda gün sonu') ,
('scott26', 'bu performansla olacak iş değil', '2024-01-07 19:00:51', "/single.html/New York borsası ABD'nin istihdam verilerinin ardından ya") ,
('alivehbi', 'olamaz', '2024-01-07 18:56:28', '/single.html/Yatırımcı rehberi (1)') ,
('scott26', 'ah be abi!', '2024-01-07 18:57:01', '/single.html/Ponzi şeması hakkında merak edilenler') ,
('alivehbi', 'milleti kandırmayı bırakın!', '2024-01-07 18:56:45', '/single.html/ISO; enerji depolama standartlarını Çin’de belirleyecek') ,
('david58', 'olamaz', '2024-01-07 18:56:45', '/single.html/Türkiye İMSAD Aylık Sektör Raporu açıklandı') ,
('nusretk', 'olamaz', '2024-01-07 18:56:28', "/single.html/Kültür ve Turizm Bakanlığınca 2023'te 400 milyondan fazla") ,
('david58', 'bu iyi haber işte!', '2024-01-07 19:00:34', '/single.html/Yatırımcı rehberi (1)') ,
('nusretk', 'bu performansla olacak iş değil', '2024-01-07 18:56:03', "/single.html/Kültür ve Turizm Bakanlığınca 2023'te 400 milyondan fazla") ,
('ugur', 'çok saçma', '2024-01-07 18:56:09', '/single.html/Ponzi şeması hakkında merak edilenler') ,
('david58', 'çok saçma', '2024-01-07 18:56:09', '/single.html/Ponzi şeması hakkında merak edilenler') ,
('david58', 'ah be abi!', '2024-01-07 19:00:34', '/single.html/Ponzi şeması hakkında merak edilenler') ,
('ugur', 'milleti kandırmayı bırakın!', '2024-01-07 18:56:28', "/single.html/Kültür ve Turizm Bakanlığınca 2023'te 400 milyondan fazla") ,
('scott26', 'ah be abi!', '2024-01-07 18:56:03', '/single.html/ISO; enerji depolama standartlarını Çin’de belirleyecek') ,
('ugur', 'beğendim bu haberi', '2024-01-07 18:56:09', '/single.html/Türkiye İMSAD Aylık Sektör Raporu açıklandı') ,
('david58', 'beğendim bu haberi', '2024-01-07 18:56:03', '/single.html/Yatırımcı rehberi (1)') ,
('nusretk', 'bu iyi haber işte!', '2024-01-07 18:56:45', '/single.html/Borsanın 10 yıllık ocak performansı') ,
('alivehbi', 'bu iyi haber işte!', '2024-01-07 19:00:51', '/single.html/Borsanın 10 yıllık ocak performansı') ,
('nusretk', 'bu performansla olacak iş değil', '2024-01-07 18:56:45', '/single.html/ISO; enerji depolama standartlarını Çin’de belirleyecek') ,
('alivehbi', 'olamaz', '2024-01-07 18:57:01', '/single.html/Türkiye İMSAD Aylık Sektör Raporu açıklandı') ,
('ugur', 'çok saçma', '2024-01-07 19:00:34', '/single.html/Piyasalarda gün sonu') ,
('david58', 'çok saçma', '2024-01-07 18:56:45', '/single.html/Piyasalarda gün sonu') ,
('nusretk', 'olamaz', '2024-01-07 19:00:34', '/single.html/Türkiye İMSAD Aylık Sektör Raporu açıklandı') ,
('scott26', 'ben böyle işi ya!', '2024-01-07 18:56:03', "/single.html/Kültür ve Turizm Bakanlığınca 2023'te 400 milyondan fazla") ,
('nusretk', 'olamaz', '2024-01-07 18:56:28', '/single.html/Piyasalarda gün sonu') ,
('ugur', 'beğendim bu haberi', '2024-01-07 19:00:34', '/single.html/Piyasalarda gün sonu') ,
('alivehbi', 'son gün için fena değil!', '2024-01-07 19:00:51', '/single.html/Ponzi şeması hakkında merak edilenler') ,
('ugur', 'bu performansla olacak iş değil', '2024-01-07 18:56:45', '/single.html/Yatırımcı rehberi (1)') ,
('alivehbi', 'milleti kandırmayı bırakın!', '2024-01-07 18:56:09', '/single.html/Türkiye İMSAD Aylık Sektör Raporu açıklandı') ,
('david58', 'bu iyi haber işte!', '2024-01-07 19:00:34', '/single.html/Piyasalarda gün sonu') ,
('ugur', 'ben böyle işi ya!', '2024-01-07 18:56:09', '/single.html/Ticaret Bakanlığı, mevzuata aykırı davranan 58 e-ticaret') ,
('scott26', 'bu iyi haber işte!', '2024-01-07 18:56:45', '/single.html/BIST 100 endeksi, günü yüzde 1,07 değer kazanarak 7.628,7') ,
('scott26', 'bu iyi haber işte!', '2024-01-07 18:56:45', '/single.html/Türkiye İMSAD Aylık Sektör Raporu açıklandı') ,
('nusretk', 'beğendim bu haberi', '2024-01-07 18:56:45', '/single.html/Piyasalarda gün sonu') ,
('scott26', 'ah be abi!', '2024-01-07 18:57:01', '/single.html/Borsanın 10 yıllık ocak performansı') ,
('david58', 'beğendim bu haberi', '2024-01-07 18:56:09', "/single.html/Kültür ve Turizm Bakanlığınca 2023'te 400 milyondan fazla") ,
('nusretk', 'bu iyi haber işte!', '2024-01-07 18:56:03', '/single.html/Türkiye İMSAD Aylık Sektör Raporu açıklandı') ,
('nusretk', 'bu iyi haber işte!', '2024-01-07 19:00:34', '/single.html/Ponzi şeması hakkında merak edilenler') ,
('alivehbi', 'son gün için fena değil!', '2024-01-07 19:00:34', "/single.html/New York borsası ABD'nin istihdam verilerinin ardından ya") ,
('nusretk', 'olamaz', '2024-01-07 18:56:45', '/single.html/Borsanın 10 yıllık ocak performansı') ,
('scott26', 'bu iyi haber işte!', '2024-01-07 18:57:01', '/single.html/BIST 100 endeksi, günü yüzde 1,07 değer kazanarak 7.628,7') ,
('alivehbi', 'bu iyi haber işte!', '2024-01-07 18:56:45', '/single.html/Borsanın 10 yıllık ocak performansı') ,
('scott26', 'beğendim bu haberi', '2024-01-07 18:56:03', '/single.html/Ponzi şeması hakkında merak edilenler') ,
('alivehbi', 'ah be abi!', '2024-01-07 18:57:01', '/single.html/Ponzi şeması hakkında merak edilenler') ,
('nusretk', 'beğendim bu haberi', '2024-01-07 19:00:51', '/single.html/Ponzi şeması hakkında merak edilenler') ,
('scott26', 'olamaz', '2024-01-07 18:56:45', '/single.html/ISO; enerji depolama standartlarını Çin’de belirleyecek') ,
('scott26', 'olamaz', '2024-01-07 18:56:45', '/single.html/Yatırımcı rehberi (1)') ,
('alivehbi', 'ah be abi!', '2024-01-07 18:56:03', '/single.html/ISO; enerji depolama standartlarını Çin’de belirleyecek') ,
('alivehbi', 'çok saçma', '2024-01-07 18:57:01', '/single.html/Yatırımcı rehberi (1)') ,
('scott26', 'çok saçma', '2024-01-07 18:56:45', '/single.html/Piyasalarda gün sonu') ,
('alivehbi', 'olamaz', '2024-01-07 18:56:45', "/single.html/New York borsası ABD'nin istihdam verilerinin ardından ya") ,
('nusretk', 'ah be abi!', '2024-01-07 18:56:45', '/single.html/Türkiye İMSAD Aylık Sektör Raporu açıklandı') ,
('david58', 'çok saçma', '2024-01-07 18:57:01', '/single.html/ISO; enerji depolama standartlarını Çin’de belirleyecek') ,
('alivehbi', 'çok saçma', '2024-01-07 19:00:51', "/single.html/Kültür ve Turizm Bakanlığınca 2023'te 400 milyondan fazla") ,
('david58', 'çok saçma', '2024-01-07 18:56:03', '/single.html/Ponzi şeması hakkında merak edilenler') ,
('nusretk', 'beğendim bu haberi', '2024-01-07 18:57:01', '/single.html/ISO; enerji depolama standartlarını Çin’de belirleyecek') ,
('scott26', 'ben böyle işi ya!', '2024-01-07 18:56:45', '/single.html/Borsanın 10 yıllık ocak performansı');
``` 
## License
`turkish-financial-website-honeypot` is licensed under the terms of the MIT license. See LICENSE for more details.
