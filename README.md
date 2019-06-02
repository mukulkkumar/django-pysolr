## Installing required packages

Ensure that the virtualenv is active and run the following from the
repository root.

```
pip install -r requirements.txt
```

## Install Apache Solr

```
apt-get install solr-tomcat
```

Update Tomcat's configuration to set the servlet connector port to a sensible
value:

```
vim /etc/tomcat7/server.xml
```

Change the value of the Catalina service's Connector port to 8983 (at the
time of writing, it defaults to 8080). Restart tomcat.

```
service tomcat6 restart
```

### Build and install the solr schema

```
python manage.py build_solr_schema > schema.xml
sudo cp schema.xml /usr/share/solr/conf/schema.xml
sudo systemctl restart tomcat7
```

Build the index for the first time:

```
python manage.py rebuild_index
```

## Haystack

```lang=json, name=haystack.json
{
    "engine": "haystack.backends.solr_backend.SolrEngine",
    "url":    "http://127.0.0.1:8983/solr"
}
```

### Update Solr Index

**Changes to the Database Aren't Reflected in Search Results**

```lang=sh
python manage.py update_index
```

This command updates the Solr index with any changes which are not currently
reflected.

If this doesn't solve the inconsistencies then you may need to resort to
using the `rebuild_index` command.

### Reindex Solr server

**When the Solr Schema Definition has been Changed**

```lang=sh
python manage.py rebuild_index
```
