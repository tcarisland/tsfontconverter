from src.tsfontconverter.fontmodel.CharacterMap import CharacterMap
from src.tsfontconverter.fontmodel.Font import Font
from src.tsfontconverter.fontmodel.Glyph import Glyph
from src.tsfontconverter.fontmodel.Meta import Meta
from src.tsfontconverter.typescript.pytsconverter import convert_subscript_type
from src.tsfontconverter.fontparser.reflectionutils import get_class_definition

font_definition = '''export interface Font {
  meta: Meta,
  name: string,
  characterMap: CharacterMap,
  type: string,
  dataUri: string
}'''
character_map_definition = '''export interface CharacterMap {
  glyphs: Glyph[],
  numberOfGlyphs: number
}'''
glyph_definition = '''export interface Glyph {
  glyphId: number,
  unicode: string
}'''
meta_definition = '''export interface Meta {
  designerUrl: string,
  licenseUrl: string,
  manufacturerUrl: string,
  description: string,
  sampleText: string
}'''


def testPytsconverter():
    a = convert_subscript_type("Dict", "Glyph")
    b = convert_subscript_type("List", "Meta")
    assert a == "Record<Glyph>"
    assert b == "Meta[]"


def test_all():
    test_font_definition()
    test_meta_definition()
    test_glyph_definition()
    test_character_map_definition()


def test_font_definition():
    tsfc_font_definition = get_class_definition(Font)
    print(tsfc_font_definition)
    assert tsfc_font_definition == font_definition


def test_character_map_definition():
    tsfc_character_map_definition = get_class_definition(CharacterMap)
    print(tsfc_character_map_definition)
    assert tsfc_character_map_definition == character_map_definition


def test_glyph_definition():
    tsfc_glyph_map_definition = get_class_definition(Glyph)
    print(tsfc_glyph_map_definition)
    assert tsfc_glyph_map_definition == glyph_definition


def test_meta_definition():
    tsfc_meta_map_definition = get_class_definition(Meta)
    print(tsfc_meta_map_definition)
    assert tsfc_meta_map_definition == meta_definition
