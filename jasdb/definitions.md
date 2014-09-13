---
layout: page
permalink: /jasdb/definitions/
title: JasDB Definitions
group: JasDB
weight: 2
tagline: JASDB
tags: [jasdb,nosql,db,document-based,storage,json,stackable,scalable,definitions,bags,entities,instances,bag,instance,database,document storage,document,REST,obera,software,oberasoftware,obera software,indexes,btree,inverted index,Java]
modified: 14-7-2014
comments: false
---

## JasDB Definitions

### Instance

An instance is what, in traditional RDBMS, would be considered a schema/database. The instance can contain a collection of Bags and has a storage path on the disk associated, meaning all bags or entities in the instance are stored in the storage location.

### Bags

The bags are a container of data, in traditional RDBMS systems these are considered tables. In this case its called a bag as its simply a big bag of data without any data definition associated. Any bag is related to an instance and the data files for the bag are stored inside the instance storage location. A bag definition can contain a number of defined indexes which will be used and maintained when data is stored or retrieved from a bag.

### SimpleEntity / Entities

This is the main storage entity used in JasDB an entity is contained inside a bag. The structure of any entity is undefined and any fields and values can be set on the entity. JasDB internally persists the entities as json format.
