from repoze.bfg.traversal import find_model
from repoze.lemonade.content import IContent
from karl.content.interfaces import ICalendarCategory
from karl.content.interfaces import ICalendarLayer
from karl.utils import find_catalog

def evolve(context):
    catalog = find_catalog(context)
    index = catalog['texts']
    for docid in index.index._docweight.keys():
        path = catalog.document_map.address_for_docid(docid)
        context = find_model(context, path)
        if (ICalendarLayer.providedBy(context) or
            ICalendarCategory.providedBy(context) or
            not IContent.providedBy(context)):
            index.unindex_doc(docid)

        if hasattr(context, '_p_deactivate'):
            context._p_deactivate()
