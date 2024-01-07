# Database Tables

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