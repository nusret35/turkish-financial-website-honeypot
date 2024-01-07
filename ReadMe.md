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

```sql
INSERT INTO comments (username, content, news_link) VALUES ('alivehbi', 'This is why I follow this news site!', 'http://127.0.0.1:5000/single.html/Yatırımcı%20rehberi%20(1)');
INSERT INTO comments (username, content, news_link) VALUES ('ekonomist', 'How reliable is this source?', 'http://127.0.0.1:5000/single.html/Yatırımcı%20rehberi%20(1)');
INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Can someone explain this further?', 'http://127.0.0.1:5000/single.html/Ticaret%20Bakanlığı,%20mevzuata%20aykırı%20davranan%2058%20e-ticaret%20firmasına%202023'te%2086,3%20milyon%20liralık%20ceza%20kesti');
INSERT INTO comments (username, content, news_link) VALUES ('ekonomist', 'More people need to know about this!', 'http://127.0.0.1:5000/single.html/Ticaret%20Bakanlığı,%20mevzuata%20aykırı%20davranan%2058%20e-ticaret%20firmasına%202023'te%2086,3%20milyon%20liralık%20ceza%20kesti');
INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'This is quite informative, thanks for sharing.', 'http://127.0.0.1:5000/single.html/Ticaret%20Bakanlığı,%20mevzuata%20aykırı%20davranan%2058%20e-ticaret%20firmasına%202023'te%2086,3%20milyon%20liralık%20ceza%20kesti');
INSERT INTO comments (username, content, news_link) VALUES ('özgür çeliktaş', 'Really interesting article!', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı');
INSERT INTO comments (username, content, news_link) VALUES ('alivehbi', 'More people need to know about this!', 'http://127.0.0.1:5000/single.html/New%20York%20borsası%20yatay%20seyirle%20kapandı');
INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'I'm not sure I understand all the implications.', 'http://127.0.0.1:5000/single.html/Ponzi%20şeması%20hakkında%20merak%20edilenler');
INSERT INTO comments (username, content, news_link) VALUES ('ugur', 'This is a great summary of the current situation.', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı');
INSERT INTO comments (username, content, news_link) VALUES ('özgür çeliktaş', 'Can someone explain this further?', 'http://127.0.0.1:5000/single.html/Ticaret%20Bakanlığı,%20mevzuata%20aykırı%20davranan%2058%20e-ticaret%20firmasına%202023'te%2086,3%20milyon%20liralık%20ceza%20kesti');
INSERT INTO comments (username, content, news_link) VALUES ('alivehbi', 'Haber kaynağı ne kadar güvenilir?', 'http://127.0.0.1:5000/single.html/Ponzi%20şeması%20hakkında%20merak%20edilenler');
INSERT INTO comments (username, content, news_link) VALUES ('ekonomist', 'Bu konu hakkında daha fazla bilgiye ihtiyacım var.', 'http://127.0.0.1:5000/single.html/Yatırımcı%20rehberi%20(1)');
INSERT INTO comments (username, content, news_link) VALUES ('alivehbi', 'Peki bu durum ekonomiyi nasıl etkileyecek?', 'http://127.0.0.1:5000/single.html/Ponzi%20şeması%20hakkında%20merak%20edilenler');
INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Bu konunun üzerinde daha fazla durulmalı.', 'http://127.0.0.1:5000/single.html/New%20York%20borsası%20yatay%20seyirle%20kapandı');
INSERT INTO comments (username, content, news_link) VALUES ('ekonomist', 'Yazarın bu konudaki uzmanlığı tartışılmaz.', 'http://127.0.0.1:5000/single.html/Yatırımcı%20rehberi%20(1)');
INSERT INTO comments (username, content, news_link) VALUES ('alivehbi', 'Etkileyici bir yazı, başka önerileriniz var mı?', 'http://127.0.0.1:5000/single.html/Yatırımcı%20rehberi%20(1)');
INSERT INTO comments (username, content, news_link) VALUES ('özgür çeliktaş', 'Yeni gelişmeleri takip etmek çok önemli.', 'http://127.0.0.1:5000/single.html/Ticaret%20Bakanlığı,%20mevzuata%20aykırı%20davranan%2058%20e-ticaret%20firmasına%202023'te%2086,3%20milyon%20liralık%20ceza%20kesti');
INSERT INTO comments (username, content, news_link) VALUES ('özgür çeliktaş', 'Yorumlarınızı ve düşüncelerinizi bekliyorum.', 'http://127.0.0.1:5000/single.html/New%20York%20borsası%20yatay%20seyirle%20kapandı');
INSERT INTO comments (username, content, news_link) VALUES ('özgür çeliktaş', 'Fikirler çok iyi ama uygulamada zorluklar olabilir.', 'http://127.0.0.1:5000/single.html/Yatırımcı%20rehberi%20(1)');
INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Haber kaynağı ne kadar güvenilir?', 'http://127.0.0.1:5000/single.html/New%20York%20borsası%20yatay%20seyirle%20kapandı');
INSERT INTO comments (username, content, news_link) VALUES ('ugur', 'Bu konu hakkında daha fazla kaynak önerir misiniz?', 'http://127.0.0.1:5000/single.html/Yatırımcı%20rehberi%20(1)');
INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Yorumlarınızı ve düşüncelerinizi bekliyorum.', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı');
INSERT INTO comments (username, content, news_link) VALUES ('ugur', 'Yorumlarınızı ve düşüncelerinizi bekliyorum.', 'http://127.0.0.1:5000/single.html/New%20York%20borsası%20yatay%20seyirle%20kapandı');
INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Etkileyici bir yazı, başka önerileriniz var mı?', 'http://127.0.0.1:5000/single.html/New%20York%20borsası%20yatay%20seyirle%20kapandı');
INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Bu konunun üzerinde daha fazla durulmalı.', 'http://127.0.0.1:5000/single.html/New%20York%20borsası%20yatay%20seyirle%20kapandı');
INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Haber kaynağı ne kadar güvenilir?', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı');
INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Gerçekten düşündürücü bir yazı olmuş.', 'http://127.0.0.1:5000/single.html/Ticaret%20Bakanlığı,%20mevzuata%20aykırı%20davranan%2058%20e-ticaret%20firmasına%202023'te%2086,3%20milyon%20liralık%20ceza%20kesti');
INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Peki bu durum ekonomiyi nasıl etkileyecek?', 'http://127.0.0.1:5000/single.html/Ticaret%20Bakanlığı,%20mevzuata%20aykırı%20davranan%2058%20e-ticaret%20firmasına%202023'te%2086,3%20milyon%20liralık%20ceza%20kesti');
INSERT INTO comments (username, content, news_link) VALUES ('özgür çeliktaş', 'Fikirler çok iyi ama uygulamada zorluklar olabilir.', 'http://127.0.0.1:5000/single.html/New%20York%20borsası%20yatay%20seyirle%20kapandı');
INSERT INTO comments (username, content, news_link) VALUES ('özgür çeliktaş', 'Bu konu hakkında daha fazla bilgiye ihtiyacım var.', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı'); ​​
INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Fikirler çok iyi ama uygulamada zorluklar olabilir.', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı');
INSERT INTO comments (username, content, news_link) VALUES ('ugur', 'Bu tür içeriklerin devamını bekliyorum.', 'http://127.0.0.1:5000/single.html/Yatırımcı%20rehberi%20(1)');
INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Bu konunun üzerinde daha fazla durulmalı.', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı');
INSERT INTO comments (username, content, news_link) VALUES ('ugur', 'Peki bu durum ekonomiyi nasıl etkileyecek?', 'http://127.0.0.1:5000/single.html/Yatırımcı%20rehberi%20(1)');
INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Bu tür içeriklerin devamını bekliyorum.', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı');
INSERT INTO comments (username, content, news_link) VALUES ('ekonomist', 'Bu konuda daha fazla insanın bilgi sahibi olması gerekiyor.', 'http://127.0.0.1:5000/single.html/Yatırımcı%20rehberi%20(1)');
INSERT INTO comments (username, content, news_link) VALUES ('ekonomist', 'Bu konuda daha fazla tartışma görmek istiyorum.', 'http://127.0.0.1:5000/single.html/Yatırımcı%20rehberi%20(1)');
INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Çok bilgilendirici bir yazı, elinize sağlık!', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı');
INSERT INTO comments (username, content, news_link) VALUES ('özgür çeliktaş', 'Yorumlarınızı ve düşüncelerinizi bekliyorum.', 'http://127.0.0.1:5000/single.html/Ticaret%20Bakanlığı,%20mevzuata%20aykırı%20davranan%2058%20e-ticaret%20firmasına%202023'te%2086,3%20milyon%20liralık%20ceza%20kesti');
INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Haber kaynağı ne kadar güvenilir?', 'http://127.0.0.1:5000/single.html/Ticaret%20Bakanlığı,%20mevzuata%20aykırı%20davranan%2058%20e-ticaret%20firmasına%202023'te%2086,3%20milyon%20liralık%20ceza%20kesti');
INSERT INTO comments (username, content, news_link) VALUES ('ekonomist', 'Yazarın bu konudaki uzmanlığı tartışılmaz.', 'http://127.0.0.1:5000/single.html/Ponzi%20şeması%20hakkında%20merak%20edilenler');
INSERT INTO comments (username, content, news_link) VALUES ('ekonomist', 'Çok bilgilendirici bir yazı, elinize sağlık!', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı');
INSERT INTO comments (username, content, news_link) VALUES ('ugur', 'Bu konu hakkında daha fazla kaynak önerir misiniz?', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı');
INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Haber kaynağı ne kadar güvenilir?', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı');
INSERT INTO comments (username, content, news_link) VALUES ('alivehbi', 'Bu konu hakkında daha fazla bilgiye ihtiyacım var.', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı');
INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Yorumlarınızı ve düşüncelerinizi bekliyorum.', 'http://127.0.0.1:5000/single.html/Yatırımcı%20rehberi%20(1)');
INSERT INTO comments (username, content, news_link) VALUES ('alivehbi', 'Fikirler çok iyi ama uygulamada zorluklar olabilir.', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı');
INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Bu konuda daha fazla insanın bilgi sahibi olması gerekiyor.', 'http://127.0.0.1:5000/single.html/Ticaret%20Bakanlığı,%20mevzuata%20aykırı%20davranan%2058%20e-ticaret%20firmasına%202023'te%2086,3%20milyon%20liralık%20ceza%20kesti');
INSERT INTO comments (username, content, news_link) VALUES ('ekonomist', 'Yeni gelişmeleri takip etmek çok önemli.', 'http://127.0.0.1:5000/single.html/Ticaret%20Bakanlığı,%20mevzuata%20aykırı%20davranan%2058%20e-ticaret%20firmasına%202023'te%2086,3%20milyon%20liralık%20ceza%20kesti');
INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Bu konu hakkında daha fazla tartışma görmek istiyorum.', 'http://127.0.0.1:5000/single.html/Ticaret%20Bakanlığı,%20mevzuata%20aykırı%20davranan%2058%20e-ticaret%20firmasına%202023'te%2086,3%20milyon%20liralık%20ceza%20kesti'); 
INSERT INTO comments (username, content, news_link) VALUES ('alivehbi', 'Haber kaynağı ne kadar güvenilir?', 'http://127.0.0.1:5000/single.html/New%20York%20borsası%20yatay%20seyirle%20kapandı');
INSERT INTO comments (username, content, news_link) VALUES ('ekonomist', 'Harika bir makale, teşekkürler!', 'http://127.0.0.1:5000/single.html/Ticaret%20Bakanlığı,%20mevzuata%20aykırı%20davranan%2058%20e-ticaret%20firmasına%202023'te%2086,3%20milyon%20liralık%20ceza%20kesti');
INSERT INTO comments (username, content, news_link) VALUES ('ugur', 'Yazarın bu konudaki uzmanlığı tartışılmaz.', 'http://127.0.0.1:5000/single.html/New%20York%20borsası%20yatay%20seyirle%20kapandı');
INSERT INTO comments (username, content, news_link) VALUES ('alivehbi', 'Bu tür içeriklerin devamını bekliyorum.', 'http://127.0.0.1:5000/single.html/Yatırımcı%20rehberi%20(1)');
INSERT INTO comments (username, content, news_link) VALUES ('özgür çeliktaş', 'Peki bu durum ekonomiyi nasıl etkileyecek?', 'http://127.0.0.1:5000/single.html/Yatırımcı%20rehberi%20(1)');
INSERT INTO comments (username, content, news_link) VALUES ('alivehbi', 'İlginç bir perspektif, daha önce hiç bu açıdan bakmamıştım.', 'http://127.0.0.1:5000/single.html/Ponzi%20şeması%20hakkında%20merak%20edilenler');
INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Harika bir makale, teşekkürler!', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı');
INSERT INTO comments (username, content, news_link) VALUES ('ugur', 'Bu tür içeriklerin devamını bekliyorum.', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı');
INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Çok bilgilendirici bir yazı, elinize sağlık!', 'http://127.0.0.1:5000/single.html/New%20York%20borsası%20yatay%20seyirle%20kapandı');
INSERT INTO comments (username, content, news_link) VALUES ('ekonomist', 'Etkileyici bir yazı, başka önerileriniz var mı?', 'http://127.0.0.1:5000/single.html/Yatırımcı%20rehberi%20(1)');
INSERT INTO comments (username, content, news_link) VALUES ('ugur', 'Bu konuda daha fazla insanın bilgi sahibi olması gerekiyor.', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı');

INSERT INTO comments (username, content, news_link) VALUES ('alivehbi', 'Haber kaynağı ne kadar güvenilir?', 'http://127.0.0.1:5000/single.html/Ticaret%20Bakanlığı,%20mevzuata%20aykırı%20davranan%2058%20e-ticaret%20firmasına%202023'te%2086,3%20milyon%20liralık%20ceza%20kesti');

INSERT INTO comments (username, content, news_link) VALUES ('ekonomist', 'Etkileyici bir yazı, başka önerileriniz var mı?', 'http://127.0.0.1:5000/single.html/Yatırımcı%20rehberi%20(1)');

INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Bu konunun üzerinde daha fazla durulmalı.', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı');

INSERT INTO comments (username, content, news_link) VALUES ('alivehbi', 'Bu konuda daha fazla tartışma görmek istiyorum.', 'http://127.0.0.1:5000/single.html/Ponzi%20şeması%20hakkında%20merak%20edilenler');

INSERT INTO comments (username, content, news_link) VALUES ('alivehbi', 'Bu tür içeriklerin devamını bekliyorum.', 'http://127.0.0.1:5000/single.html/New%20York%20borsası%20yatay%20seyirle%20kapandı');

INSERT INTO comments (username, content, news_link) VALUES ('özgür çeliktaş', 'Peki bu durum ekonomiyi nasıl etkileyecek?', 'http://127.0.0.1:5000/single.html/New%20York%20borsası%20yatay%20seyirle%20kapandı');

INSERT INTO comments (username, content, news_link) VALUES ('özgür çeliktaş', 'Bu konunun üzerinde daha fazla durulmalı.', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı');

INSERT INTO comments (username, content, news_link) VALUES ('ekonomist', 'Gerçekten düşündürücü bir yazı olmuş.', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı');

INSERT INTO comments (username, content, news_link) VALUES ('özgür çeliktaş', 'Yeni gelişmeleri takip etmek çok önemli.', 'http://127.0.0.1:5000/single.html/Ponzi%20şeması%20hakkında%20merak%20edilenler');

INSERT INTO comments (username, content, news_link) VALUES ('ugur', 'Bu konu hakkında daha fazla kaynak önerir misiniz?', 'http://127.0.0.1:5000/single.html/Yatırımcı%20rehberi%20(1)');",

INSERT INTO comments (username, content, news_link) VALUES ('ugur', 'Bu konu hakkında daha fazla bilgiye ihtiyacım var.', 'http://127.0.0.1:5000/single.html/New%20York%20borsası%20yatay%20seyirle%20kapandı');

INSERT INTO comments (username, content, news_link) VALUES ('alivehbi', 'Harika bir makale, teşekkürler!', 'http://127.0.0.1:5000/single.html/New%20York%20borsası%20yatay%20seyirle%20kapandı');

INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Yorumlarınızı ve düşüncelerinizi bekliyorum.', 'http://127.0.0.1:5000/single.html/Ticaret%20Bakanlığı,%20mevzuata%20aykırı%20davranan%2058%20e-ticaret%20firmasına%202023'te%2086,3%20milyon%20liralık%20ceza%20kesti');

INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Etkileyici bir yazı, başka önerileriniz var mı?', 'http://127.0.0.1:5000/single.html/Yatırımcı%20rehberi%20(1)');

INSERT INTO comments (username, content, news_link) VALUES ('alivehbi', 'Bence bu konuda daha derinlemesine bir analiz gerekiyor.', 'http://127.0.0.1:5000/single.html/Ticaret%20Bakanlığı,%20mevzuata%20aykırı%20davranan%2058%20e-ticaret%20firmasına%202023'te%2086,3%20milyon%20liralık%20ceza%20kesti');

INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Peki bu durum ekonomiyi nasıl etkileyecek?', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı');

INSERT INTO comments (username, content, news_link) VALUES ('özgür çeliktaş', 'Yazarın bu konudaki uzmanlığı tartışılmaz.', 'http://127.0.0.1:5000/single.html/New%20York%20borsası%20yatay%20seyirle%20kapandı');

INSERT INTO comments (username, content, news_link) VALUES ('alivehbi', 'Yorumlarınızı ve düşüncelerinizi bekliyorum.', 'http://127.0.0.1:5000/single.html/Yatırımcı%20rehberi%20(1)');

INSERT INTO comments (username, content, news_link) VALUES ('özgür çeliktaş', 'Bence bu konuda daha derinlemesine bir analiz gerekiyor.', 'http://127.0.0.1:5000/single.html/Ticaret%20Bakanlığı,%20mevzuata%20aykırı%20davranan%2058%20e-ticaret%20firmasına%202023'te%2086,3%20milyon%20liralık%20ceza%20kesti');

INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Bu bilgiler ışığında ne yapmalıyız?', 'http://127.0.0.1:5000/single.html/Ticaret%20Bakanlığı,%20mevzuata%20aykırı%20davranan%2058%20e-ticaret%20firmasına%202023'te%2086,3%20milyon%20liralık%20ceza%20kesti');

INSERT INTO comments (username, content, news_link) VALUES ('ugur', 'Bu konunun üzerinde daha fazla durulmalı.', 'http://127.0.0.1:5000/single.html/New%20York%20borsası%20yatay%20seyirle%20kapandı');

INSERT INTO comments (username, content, news_link) VALUES ('özgür çeliktaş', 'Bu bilgiler gerçekten çok yararlı oldu.', 'http://127.0.0.1:5000/single.html/Ticaret%20Bakanlığı,%20mevzuata%20aykırı%20davranan%2058%20e-ticaret%20firmasına%202023'te%2086,3%20milyon%20liralık%20ceza%20kesti');

INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Bu konuda daha fazla insanın bilgi sahibi olması gerekiyor.', 'http://127.0.0.1:5000/single.html/Ticaret%20Bakanlığı,%20mevzuata%20aykırı%20davranan%2058%20e-ticaret%20firmasına%202023'te%2086,3%20milyon%20liralık%20ceza%20kesti');

INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Çok bilgilendirici bir yazı, elinize sağlık!', 'http://127.0.0.1:5000/single.html/Ponzi%20şeması%20hakkında%20merak%20edilenler');

INSERT INTO comments (username, content, news_link) VALUES ('özgür çeliktaş', 'Bence bu konuda daha derinlemesine bir analiz gerekiyor.', 'http://127.0.0.1:5000/single.html/Ticaret%20Bakanlığı,%20mevzuata%20aykırı%20davranan%2058%20e-ticaret%20firmasına%202023'te%2086,3%20milyon%20liralık%20ceza%20kesti');

INSERT INTO comments (username, content, news_link) VALUES ('alivehbi', 'Bu bilgiler ışığında ne yapmalıyız?', 'http://127.0.0.1:5000/single.html/New%20York%20borsası%20yatay%20seyirle%20kapandı');

INSERT INTO comments (username, content, news_link) VALUES ('özgür çeliktaş', 'Gerçekten düşündürücü bir yazı olmuş.', 'http://127.0.0.1:5000/single.html/Yatırımcı%20rehberi%20(1)');

INSERT INTO comments (username, content, news_link) VALUES ('ekonomist', 'Bu konuda daha fazla insanın bilgi sahibi olması gerekiyor.', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı');

INSERT INTO comments (username, content, news_link) VALUES ('ugur', 'Bu bilgiler gerçekten çok yararlı oldu.', 'http://127.0.0.1:5000/single.html/Ponzi%20şeması%20hakkında%20merak%20edilenler');

INSERT INTO comments (username, content, news_link) VALUES ('ugur', 'Etkileyici bir yazı, başka önerileriniz var mı?', 'http://127.0.0.1:5000/single.html/Ticaret%20Bakanlığı,%20mevzuata%20aykırı%20davranan%2058%20e-ticaret%20firmasına%202023'te%2086,3%20milyon%20liralık%20ceza%20kesti');

INSERT INTO comments (username, content, news_link) VALUES ('ugur', 'Yorumlarınızı ve düşüncelerinizi bekliyorum.', 'http://127.0.0.1:5000/single.html/New%20York%20borsası%20yatay%20seyirle%20kapandı');

INSERT INTO comments (username, content, news_link) VALUES ('alivehbi', 'Yorumlarınızı ve düşüncelerinizi bekliyorum.', 'http://127.0.0.1:5000/single.html/Ponzi%20şeması%20hakkında%20merak%20edilenler');

INSERT INTO comments (username, content, news_link) VALUES ('ekonomist', 'Bu konu hakkında daha fazla kaynak önerir misiniz?', 'http://127.0.0.1:5000/single.html/New%20York%20borsası%20yatay%20seyirle%20kapandı');

INSERT INTO comments (username, content, news_link) VALUES ('ekonomist', 'Bu konuda daha fazla insanın bilgi sahibi olması gerekiyor.', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı');
INSERT INTO comments (username, content, news_link) VALUES ('alivehbi', 'Bu bilgiler gerçekten çok yararlı oldu.', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı');

INSERT INTO comments (username, content, news_link) VALUES ('ekonomist', 'Fikirler çok iyi ama uygulamada zorluklar olabilir.', 'http://127.0.0.1:5000/single.html/Ponzi%20şeması%20hakkında%20merak%20edilenler');

INSERT INTO comments (username, content, news_link) VALUES ('nusret', 'Harika bir makale, teşekkürler!', 'http://127.0.0.1:5000/single.html/Yatırımcı%20rehberi%20(1)');

INSERT INTO comments (username, content, news_link) VALUES ('ekonomist', 'Bu bilgiler ışığında ne yapmalıyız?', 'http://127.0.0.1:5000/single.html/Küresel%20piyasalar,%20ABD%20enflasyon%20verilerine%20odaklandı');

INSERT INTO comments (username, content, news_link) VALUES ('ugur', 'Bu konuda daha fazla tartışma görmek istiyorum.', 'http://127.0.0.1:5000/single.html/New%20York%20borsası%20yatay%20seyirle%20kapandı');

```
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
