---
layout: page
permalink: /developers/
title: Developers
modified: 14-07-2014
weight: 1
comments: false
tags: [jasdb,nosql,db,document-based,storage,json,stackable,scalable,definitions,bags,entities,instances,bag,instance,database,document storage,document,REST,obera,software,oberasoftware,obera software,indexes,btree,inverted index,Java]
---
We have open sourced the core of our JasDB product, if you are a developer you are welcome to help us take JasDB to the next level. The JasDB Open Source version is hosted in two bitbucket repositories which are publicly available.

### GIT Repositories
This is the main repository:

{% highlight java %}
git clone https://bitbucket.org/oberasoftware/jasdb_open/
{% endhighlight %}

This repository contains the extension API definitions for JasDB
{% highlight java %}
git clone https://bitbucket.org/oberasoftware/jasdb_core/
{% endhighlight %}

### Becoming a developer
If you want to participate in developing JasDB we recruit developers by reviewing proposed pull requests before granting write access to the main repositories. If you want to participate simply suggest changes to JasDB by providing a pull request with the proposed changes, make sure the description of the pull request contains an accurate description of the changes.

### Building JasDB
In order to build JasDB, you will require the following pre-requisites:

* Java 1.7
* Maven 3.0

Please make sure your JAVA_HOME and M2_HOME are set correctly. Start the build process by simply doing a

{% highlight java %}
  mvn clean install
{% endhighlight %}
