---
layout: page
permalink: /downloads/
title: JasDB Downloads
tagline: JASDB
weight: 1
tags: [jasdb,nosql,db,document-based,storage,json,stackable,scalable,definitions,bags,entities,instances,bag,instance,database,document storage,document,REST,obera,software,oberasoftware,obera software,indexes,btree,inverted index,Java]
modified: 14-7-2014
comments: false
---

## Downloads
This page contains the download links for the free Enterprise versions of JasDB. Please check the wiki for info on how to use the downloads provided to get started. The download contains both the REST client libraries and Enterprise JasDB server.

### Stable version:

* [JasDB v1.0](https://bitbucket.org/oberasoftware/jasdb_open/downloads/jasdb_1.0.zip)
* [Java API DOCS](http://oberasoftware.github.io/jasdb/apidocs/)

### Archived versions:

* [JasDB v0.8](https://bitbucket.org/oberasoftware/jasdb_open/downloads/jasdb_0.8.zip)
* [JasDB v0.7.1](https://bitbucket.org/oberasoftware/jasdb_open/downloads/jasdb_0.7.1.zip)
* [JasDB v0.7](https://bitbucket.org/oberasoftware/jasdb_open/downloads/jasdb_0.7.zip)
* [JasDB v0.6.6](https://bitbucket.org/oberasoftware/jasdb_open/downloads/jasdb_0.6.6.0.zip)
* [JasDB v0.6.5](https://bitbucket.org/oberasoftware/jasdb_open/downloads/cdlayout_0.6.5.zip)
* [JasDB v0.6.4](https://bitbucket.org/oberasoftware/jasdb_open/downloads/cdlayout_0.6.4.0.zip)

### Maven Artifacts

For Release 1.0 and above all artefacts are deployed to Maven Central, no need to specify an explicit repository.

**Legacy repository:**

Legacy release repository (0.8.x and below versions)
{% highlight xml %}
<repository>
  <id>jasdb-release</id>
  <name>JasDB release repository</name>
  <url>https://raw.github.com/oberasoftware/jasdb_release/mvn-repo</url>
</repository>
{% endhighlight %}

If you want to use the REST client for JasDB add the following dependency to your pom file:
{% highlight xml %}
<dependency>
   <groupId>com.oberasoftware</groupId>
   <artifactId>jasdb_restconnector</artifactId>
   <version>1.0</version>
</dependency>
{% endhighlight %}

When you want to run JasDB inside your application without using REST the following dependency is needed:
{% highlight xml %}
<dependency>
   <groupId>com.oberasoftware</groupId>
   <artifactId>jasdb_localservice</artifactId>
   <version>1.0</version>
</dependency>
{% endhighlight %}
