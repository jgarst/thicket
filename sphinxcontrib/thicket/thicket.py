from pathlib import Path

from docutils.nodes import Element, inline
from docutils.parsers.rst import Directive

from typing import Tuple

from sphinx.roles import XRefRole
from sphinx.addnodes import pending_xref
from sphinx.domains import Domain, ObjType
from sphinx.environment import BuildEnvironment
from sphinx.util import ws_re, docname_join
from sphinx.util.nodes import clean_astext, make_refnode
from sphinx.locale import _
from sphinx.builders import Builder


class backlinks(Element):
    pass


class BacklinksDirective(Directive):
    """A directive that displays all notes that link here."""

    def run(self):
        raise NotImplementedError
        return [backlinks("")]


# Sphinx traditionally talks about the :doc: role in terms of
# `path` and `explicit title <path>`.  This role reverses those inputs,
# interpreting one argument as `title` and two as `title <explicit path>`.
# In the case when there is no path, Thicket will interpret title to find a
# path based on global configuration.
class BacklinkRole(XRefRole):
    """
    A role like :doc: that links to a document in the /documents folder when
    referencing a `title`, or to an explicitly given path when referencing
    `title <explicit path>`.

    When interpreted as paths, titles are casefolded and have continuous
    whitespace replaced with an underscore.

    The class is named for an intent to create backlinks to all sources that
    reference a destination document, but that is not implemented yet.
    """

    def process_link(
        self,
        env: BuildEnvironment,
        refnode: Element,
        has_explicit_target: bool,
        title: str,
        target: str,
    ) -> Tuple[str, str]:
        """
        Runs after parsing the backlink target and title text of the thicket
        link, and finds the correct note given the `documents/` folder
        convention
        """

        if has_explicit_target:
            note_path = target
        else:
            filename = ws_re.sub("_", target).casefold()
            note_path = str(Path("/documents", filename))

        return title, note_path


class ThicketDomain(Domain):
    """The namespace for Thicket notes."""

    name = "t"
    label = "Thicket"

    object_types = {
        "doc": ObjType(_("document"), "doc", searchprio=-1),
    }

    roles = {
        "link": BacklinkRole(warn_dangling=True, innernodeclass=inline),
    }

    def resolve_xref(
        self,
        env: BuildEnvironment,
        fromdocname: str,
        builder: Builder,
        typ: str,
        target: str,
        node: pending_xref,
        contnode: Element,
    ) -> Element:

        return (
            self._resolve_doc_xref(
                env, fromdocname, builder, typ, target, node, contnode
            )
            if typ == "link"
            else None
        )

    # XXX: My theory is that I want to write my own resolver for notes
    #      This is a copy of the std document resolver to get started.
    def _resolve_doc_xref(
        self,
        env: BuildEnvironment,
        fromdocname: str,
        builder: Builder,
        typ: str,
        target: str,
        node: pending_xref,
        contnode: Element,
    ) -> Element:
        """XXX copied from sphinx/sphinx/domains/std.py XXX"""
        # directly reference to document by source name
        # can be absolute or relative
        refdoc = node.get("refdoc", fromdocname)
        docname = docname_join(refdoc, node["reftarget"])
        if docname not in env.all_docs:
            return None
        else:
            if node["refexplicit"]:
                # reference with explicit title
                caption = node.astext()
            else:
                caption = clean_astext(env.titles[docname])
            innernode = inline(caption, caption, classes=["doc"])
            return make_refnode(builder, fromdocname, docname, None, innernode)


def setup(app):
    app.add_domain(ThicketDomain)

    return {
        "version": "0.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
