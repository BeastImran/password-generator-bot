# Encryption

This [encryption.md]() file explain the way i have used encryption to store notes (data) of users.

# Library used

As i am using python and being a nood in area i have used [cryptography](https://pypi.org/project/cryptography/) module's [cryptography.fernet](https://cryptography.io/en/latest/fernet.html) module which is guess is popular to generate keys and provide basic functionalities like encrypt and decrypt.

This library can be install using the pip command as shown below.

```bash
pip install cryptography
```

# Data encryption

* Fernet provides a really random and long key each time you call the function. Keys generated usually look like the one below.

  key is generated in binary string format which look like below:
  
  ![generated key](https://github.com/BeastImran/password-generator-bot/blob/main/images/generated_key.png "generated key")
  
* These keys can be used to encrypt any binary data you provide to fernet's encrypt function which will use the key provided.

  the data after encryption are stored in database as below with their entry time:
  
  ![saved encrypted notes](https://github.com/BeastImran/password-generator-bot/blob/main/images/stored_encrypted_notes.png "saved encrypted notes")

* Any data encrypted can be decrypted using the same key by which it was encrypted!, so, which raises a serious question. 

        Q) what will happen if some how the key gets leaked?

        Ans) The honest answer is that the data can be decrypted by anyone using that key.

* There was a single point of failure which really wasn't a good thing.

* So decided to use unique keys to each user and a secret sauce to mess up the key so that even if the key would be leaked it would effect only one user and others will and can be saved with their unique keys messed up with secret sauce.

* It decreased the threat surface atleast a little. Well there still are some (a lot of) loop holes to work around the system and i am working on them already.

* The main aim was to somehow encrypt data maintain the date secure enough for this kind of small, honestly really small project.

# Secret sauce

Well secret should be secret, so that's why i will not be including the encryption implementation files in public.

If anyone want to take a look at them, or suggest a better way to encrypt and maintain keys, can reach out to me thourgh telegram [@BeastImran](https://t.me/beastimran).

