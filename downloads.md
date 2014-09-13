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

### Downloads
This page contains the download links for the free Enterprise versions of JasDB. Please check the wiki for info on how to use the downloads provided to get started. The download contains both the REST client libraries and Enterprise JasDB server.

#### Stable version:

* [JasDB v0.8](https://bitbucket.org/oberasoftware/jasdb_open/downloads/jasdb_0.8.zip)

#### Archived versions:

* [JasDB v0.7.1](https://bitbucket.org/oberasoftware/jasdb_open/downloads/jasdb_0.7.1.zip)
* [JasDB v0.7](https://bitbucket.org/oberasoftware/jasdb_open/downloads/jasdb_0.7.zip)
* [JasDB v0.6.6](https://bitbucket.org/oberasoftware/jasdb_open/downloads/jasdb_0.6.6.0.zip)
* [JasDB v0.6.5](https://bitbucket.org/oberasoftware/jasdb_open/downloads/cdlayout_0.6.5.zip)
* [JasDB v0.6.4](https://bitbucket.org/oberasoftware/jasdb_open/downloads/cdlayout_0.6.4.0.zip)

#### Maven Artifacts

In order to obtain the maven release artifacts the following repository can be used:
{% highlight xml %}
<repository>
  <id>renarj-release</id>
  <name>Internal release repository</name>
  <url>http://oberasoftware.com:8080/nexus/content/repositories/ren_release/</url>
</repository>
{% endhighlight %}

If you want to use the REST client for JasDB add the following dependency to your pom file:
{% highlight xml %}
<dependency>
   <groupId>nl.renarj</groupId>
   <artifactId>jasdb_restconnector</artifactId>
   <version>0.8</version>
</dependency>
{% endhighlight %}

When you want to run JasDB inside your application without using REST the following dependency is needed:
{% highlight xml %}
<dependency>
   <groupId>nl.renarj</groupId>
   <artifactId>jasdb_localservice</artifactId>
   <version>0.8</version>
</dependency>
{% endhighlight %}
