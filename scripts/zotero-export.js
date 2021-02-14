// This script should be pasted into Zotero
// under Edit > Preferences > Better Bibtex > Advanced > postscript

switch (Translator.header.label) {
  case 'Better BibLaTeX':
    Zotero.debug("DEBUGGING: "+JSON.stringify(item.relations["dc:relation"]))
    if (item.relations["dc:relation"]){
        Zotero.debug("DEBUGGING: "+JSON.stringify(
            Zotero,
            function(key, value) { 
              if (typeof value === 'function') {
                 return value.toString();
              } else {
                 return value;
              }
		}));
        reference.add({
            name: 'related', 
            value: item.relations["dc:relation"][0].substring(39)
        })
    }

    break;
  case 'Better BibTeX':
    if (item.itemType=='software'){
		reference={}
	};
    break;
  case 'Better CSL JSON':
    break;
  case 'Better CSL YAML':
    reference['programming-language']=item.programmingLanguage;
    reference['type'] = item.type;
    reference.system = reference.medium;
    // reference.rights = item.rights;
    delete reference.medium;
    break;
}


