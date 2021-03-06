Mapping Format
==============

The mapping format is described by a [JSON Schema](http://json-schema.org) [document](../geordi/schema/mapping.json) in the repository.

One bit of note is that some places MusicBrainz has joint fields that aren't joint in other data sources. For a relatively complete example, take artists: depending on the source, they might be provided as MusicBrainz-type artist + credit + join phrase sets, or as artists independently, or as a complete rendered credit without splitting, or a combination of the above (a list of artists plus a complete rendered credit is especially common). Other cases include mediums and their contained tracks/formats, labels and catalog numbers, and release events/dates/countries of release. For these cases, the mapping format includes 'combined', 'split', and 'unsplit' formats: 'combined' is the target format (like MusicBrainz), 'split' is for separated lists (such as when a list of labels and a list of catalog numbers are provided, but they aren't paired), and 'unsplit' is when the data is a single list, but more joined together than the final form (such as a list of fully-rendered artist credits).
