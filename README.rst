=======
Thicket
=======
*Personal notes for densely connected ideas.*

Thicket can be used to take notes as you work, creating a wiki like resource
that is:

- Entirely text, can be managed in source control.
- Finely interlinked and quoted, with no broken links.
- Easy to browse, easy to extend.
- Structured for external tools.

Currently there is nothing here, and you shouldn't use it.
The code is a default sphinx project that is finding itself.
I encourage you to investigate Obsidian_ or Roam_ if the idea is appealing.


====
Plan
====

- ☑ Define a custom role for links to documents.
- ☐ List all backlinks at the bottom of all documents.
- ☐ Create restrictions on how documents should be structured.

  - There is a daily-notes page named with today's date.
  - Referenced documents always exist.

- ☐  Extend backlinks to support section level anchors.
- ☐  Support transclusion and other poorly named ideas.
- ☐  Create a graph visualization for notes.


===================
Potential Use Cases
===================

- Can I create a Thicket that is a valuable artifact for someone else?
- Can I create a workshop or tutorial in Thicket?
- Can I embed flashcards, versioned information, or other structured data in
  Thicket?
- Can I create editor level tools to reduce the cognitive load of taking notes?

=======
Why Not
=======
- Obsidian

  - Markdown is Calvinball, hard to extend, port and reuse.
  - I'm not thrilled with another electron app in my life.
  - Plugin API not finalized / Immature.

- Roam

  - Proprietary markdown is especially Calvinball
  - Their site does not appear to be holding it together
  - Our Beautiful Journey incoming

- MediaWiki

  - One of my primary goals is to not require a database.
  - The `Labeled Section Transclusion`_ extension exists.

- Tiddlywiki

  - A single file application makes it difficult to access and reuse structured
    information.
  - A lot of tiddlywiki's goals are similar to mine.

- Your Favorite Wiki

  - Is probably more interested in providing a complete application than a html
    representation of a set of files.

  - Thicket wants to be maintained in source control.  Your favorite wiki
    probably doesn't.

- Notion

  - Transclusion might be supported but isn't yet.
  - Intended for enterprise and not for me.
  - Probably not getting my data and workflow out in one piece.


=========
Resources
=========

- `Doug Hellman`_ blogs about his sphinx contributions


.. _Obsidian: https://obsidian.md/
.. _Roam: https://roamresearch.com/
.. _`Labeled Section Transclusion`: https://www.mediawiki.org/wiki/Extension:Labeled_Section_Transclusion
.. _`Doug Hellman`: https://doughellmann.com/
