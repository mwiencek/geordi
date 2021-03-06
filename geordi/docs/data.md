Geordi data structure
=====================

Geordi has a particular way of storing and processing data. This document will provide a conceptual overview of the various objects and their relations, and then a short description of where and how the various objects (and their relations) are stored.

Geordi objects
--------------

The core object of geordi is the 'item'. This is geordi's overarching container for entities of all sorts: releases, artists, labels, places, areas, whatever. Items have an id, a nominal type (roughly: "we think this is a release" or "we think this is an artist"), and a map -- that is, data in a standard format defining the entity. 

Conceptually contained by items are what I'll call "data items". In older versions of geordi, these were the primary object: a bit of data from a specific source with a specific identifier. This includes data that's derived from broader items, for example in a data source that only provides data files for releases, it is still often possible to extract information identifying and describing an artist, or a recording. (formerly, these derived data items were referred to separately, as 'subitems'). Upon initial insertion to geordi, each data item is made member of exactly one item. Eventually it should be possible to merge items together (or, perhaps more accurately, match items within geordi to each other -- for example, the same artist as represented in two different data sources). Data items cannot be directly linked to anything except items, since items represent the links between data items other than equivalence. However, data items carry most of the actual data in geordi, so many things are derived from them.

The third basic object that doesn't represent some sort of relation is a user. Users represent both human users who log in via MB and automatic processes indigenous to geordi.

Geordi relations
----------------

As the core of the data model, items form one side of most links. Most basically, items can be linked to other items and are assigned a type by what path in the mapped data they're assigned to (for, say, release artists, works for recordings, and more detailed data like composers, tributes, etc. -- item-item links in geordi coalesce over both ARs and more "intrinsic" links such as track recordings, release groups, etc.). This information is generally derived from data items: the data source lists that release 58729 has artists 12493 and 28359, so a release artist type link will be inserted between the item that contains release 58729 and the two items that respectively contain artists 12493 and 28359. There are, however, a small number of cases where a link will be created on implication (and possibly without any inherent data associated with one side of the link) -- since all releases have a release group, for example, it's possible that users will want to mark two items not as the same release, but as the same release group, even if the data source doesn't have a concept of a release group. Similarly, two recording items might be the same work, two places, artists, labels, etc. might be in the same area, two releases, recordings, or works might be by (for various definitions of 'by') the same artist, and many more esoteric combinations such as "these two works both have composers from the same country". To represent these sorts of connections, intermediate items with no data items might be created.

More complicated, but of course rather important, are links to entities within MusicBrainz. These present a lot of complication for the simple reason that they can often be represented, in various ways, from both geordi and from MusicBrainz. To simplify things somewhat, I'll first talk about what I call 'raw matches': that is, matches stored with geordi, that have no equivalent inverse way to be stored in MusicBrainz (perhaps a dataset derived from a private site that can't be linked to with URL relationships). These can simply connect the item, an mbid+type, a user, and a timestamp. In order to ensure it's possible to both match an item to multiple MB entities (say, for a collaboration artist) and to, when necessary, supersede old matches, raw matches can also store a value to designate if they're still valid.

However, many sorts of matches can be represented directly within MusicBrainz -- whether by a URL relationship to the relevant page of the website of the data source, or by way of an identifier such as a catalog number. Where this is possible, it's definitely preferred: ultimately, geordi's goals prefer data in MusicBrainz to data only in geordi. Luckily, the same information is possible to derive from a copy of the MusicBrainz database (presumably replicated, where it's not possible to connect directly to the production database) -- most tables in MB have a last_updated column for a timestamp, and obviously the MBID. To connect these with an item, whatever piece of data connects the item to MB must appear in the item's map, but if it's information that can be stored in MB it should always be there anyway! User is harder to determine, so such matches can just use a user corresponding to an automatic process (one per data source). The initial version will not include this sort of match, however, as it's more complex to implement.

Technical details
-----------------

All data for geordi is stored in the new geordi SQL database, or in a replicated MusicBrainz database when, in the future, non-raw matches are implemented. This data is propagated to a search server, similar to the main MusicBrainz search server except updated live (on import/remapping and when matches are registered).

The [geordi SQL schema](../sql/tables.sql) is available for consideration.
