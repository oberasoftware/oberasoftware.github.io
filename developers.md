---
layout: page
permalink: /developers/
title: Developers
modified: 22-05-2015
weight: 1
comments: false
tags: [jasdb,nosql,db,document-based,storage,json,stackable,scalable,definitions,bags,entities,instances,bag,instance,database,document storage,document,REST,obera,software,oberasoftware,obera software,indexes,btree,inverted index,Java]
---
We have open sourced the core of our JasDB product, if you are a developer you are welcome to help us take JasDB to the next level. The JasDB Open Source version is hosted in a single Github repository which is publicly available.

### GIT Repositories
This is the main repository, the master branch is the main point for active development:

{% highlight java %}
git clone https://github.com/oberasoftware/jasdb.git
{% endhighlight %}

### Becoming a developer
If you want to participate in developing JasDB we recruit developers by reviewing proposed pull requests before granting write access to the main repositories. If you want to participate simply suggest changes to JasDB by providing a pull request with the proposed changes, make sure the description of the pull request contains an accurate description of the changes.

### Building JasDB
In order to build JasDB, you will require the following pre-requisites:

* Java 1.8
* Maven 3.x

Please make sure your JAVA_HOME and M2_HOME are set correctly. Start the build process by simply doing a

{% highlight java %}
  mvn clean install
{% endhighlight %}
