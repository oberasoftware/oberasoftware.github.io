---
layout: page
permalink: /downloads/
title: JasDB Downloads
tagline: JASDB
weight: 1
tags: [jasdb,nosql,db,document-based,storage,json,stackable,scalable,definitions,bags,entities,instances,bag,instance,database,document storage,document,REST,obera,software,oberasoftware,obera software,indexes,btree,inverted index,Java]
modified: 01-07-2015
comments: false
---

## Downloads
This page contains the download links for the free Enterprise versions of JasDB. Please check the wiki for info on how to use the downloads provided to get started. The download contains both the REST client libraries and Enterprise JasDB server.

### Stable version:
* [JasDB v1.1](https://github.com/oberasoftware/jasdb-open/releases/download/1.1-6/jasdb_1.1.zip)
* [JasDB v1.1 Sources](https://github.com/oberasoftware/jasdb-open/archive/1.1-6.tar.gz)
* [Java API DOCS](http://oberasoftware.github.io/jasdb/apidocs/)

### Archived versions:
* [JasDB v1.0](https://github.com/oberasoftware/jasdb-open/releases/download/v1.0/jasdb_1.0.zip)
* [JasDB v1.0 Sources](https://github.com/oberasoftware/jasdb-open/archive/v1.0.tar.gz)
* [JasDB v0.8](https://github.com/oberasoftware/jasdb-open/releases/download/v0.8/jasdb_0.8.zip)

### Maven Artifacts

For Release 1.x and above all artefacts are deployed to Maven Central, no need to specify an explicit repository.

If you want to use the REST client for JasDB add the following dependency to your pom file:
{% highlight xml %}
<dependency>
   <groupId>com.oberasoftware</groupId>
   <artifactId>jasdb_restconnector</artifactId>
   <version>1.1</version>
</dependency>
{% endhighlight %}

When you want to run JasDB inside your application without using REST the following dependency is needed:
{% highlight xml %}
<dependency>
   <groupId>com.oberasoftware</groupId>
   <artifactId>jasdb_localservice</artifactId>
   <version>1.1</version>
</dependency>
{% endhighlight %}

**Legacy repository:**

Legacy release repository (0.8.x and below versions)
{% highlight xml %}
<repository>
  <id>jasdb-release</id>
  <name>JasDB release repository</name>
  <url>https://raw.github.com/oberasoftware/jasdb_release/mvn-repo</url>
</repository>
{% endhighlight %}

