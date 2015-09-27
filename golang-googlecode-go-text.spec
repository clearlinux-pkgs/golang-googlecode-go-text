Name     : golang-googlecode-go-text 
Version  : 0 
Release  : 1
URL      : https://github.com/golang/text/archive/601048ad6acbab6cedd582db09b8c4839ff25b15.tar.gz
Source0  : https://github.com/golang/text/archive/601048ad6acbab6cedd582db09b8c4839ff25b15.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
BuildRequires : go

%description
This repository holds supplementary Go libraries for text processing, many involving Unicode.

%prep
%setup -q -n text-601048ad6acbab6cedd582db09b8c4839ff25b15

%build

%install
%global gopath /usr/lib/golang
%global library_path golang.org/x/text
rm -rf %{buildroot}
# Copy all *.go and *.s files
install -d -p %{buildroot}%{gopath}/src/%{library_path}/
for ext in go s; do
    for file in $(find . -iname "*.$ext") ; do
         install -d -p %{buildroot}%{gopath}/src/%{library_path}/$(dirname $file)
         cp -pav $file %{buildroot}%{gopath}/src/%{library_path}/$file
    done
done
# Copy extra files 
for file in $(find ./encoding/testdata -iname "*.txt"); do
    install -d -p %{buildroot}%{gopath}/src/%{library_path}/encoding/testdata
    cp -pav $file %{buildroot}%{gopath}/src/%{library_path}/$file
done


%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export GOPATH=%{buildroot}%{gopath}
go test %{library_path}/cases
go test %{library_path}/cldr
go test %{library_path}/collate
go test %{library_path}/collate/build
go test %{library_path}/collate/colltab
go test %{library_path}/currency
go test %{library_path}/display
go test %{library_path}/encoding
go test %{library_path}/encoding/htmlindex
go test %{library_path}/internal || : 
go test %{library_path}/internal/colltab
go test %{library_path}/internal/tag
go test %{library_path}/internal/triegen
go test %{library_path}/internal/ucd
go test %{library_path}/language || :
go test %{library_path}/runes
go test %{library_path}/search
go test %{library_path}/transform
go test %{library_path}/unicode/norm
go test %{library_path}/unicode/rangetable
go test %{library_path}/width

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/golang.org/x/text/cases/cases.go
/usr/lib/golang/src/golang.org/x/text/cases/context.go
/usr/lib/golang/src/golang.org/x/text/cases/context_test.go
/usr/lib/golang/src/golang.org/x/text/cases/example_test.go
/usr/lib/golang/src/golang.org/x/text/cases/gen.go
/usr/lib/golang/src/golang.org/x/text/cases/gen_trieval.go
/usr/lib/golang/src/golang.org/x/text/cases/map.go
/usr/lib/golang/src/golang.org/x/text/cases/map_test.go
/usr/lib/golang/src/golang.org/x/text/cases/tables.go
/usr/lib/golang/src/golang.org/x/text/cases/tables_test.go
/usr/lib/golang/src/golang.org/x/text/cases/trieval.go
/usr/lib/golang/src/golang.org/x/text/cldr/base.go
/usr/lib/golang/src/golang.org/x/text/cldr/cldr.go
/usr/lib/golang/src/golang.org/x/text/cldr/cldr_test.go
/usr/lib/golang/src/golang.org/x/text/cldr/collate.go
/usr/lib/golang/src/golang.org/x/text/cldr/collate_test.go
/usr/lib/golang/src/golang.org/x/text/cldr/data_test.go
/usr/lib/golang/src/golang.org/x/text/cldr/decode.go
/usr/lib/golang/src/golang.org/x/text/cldr/examples_test.go
/usr/lib/golang/src/golang.org/x/text/cldr/makexml.go
/usr/lib/golang/src/golang.org/x/text/cldr/resolve.go
/usr/lib/golang/src/golang.org/x/text/cldr/resolve_test.go
/usr/lib/golang/src/golang.org/x/text/cldr/slice.go
/usr/lib/golang/src/golang.org/x/text/cldr/slice_test.go
/usr/lib/golang/src/golang.org/x/text/cldr/xml.go
/usr/lib/golang/src/golang.org/x/text/collate/build/builder.go
/usr/lib/golang/src/golang.org/x/text/collate/build/builder_test.go
/usr/lib/golang/src/golang.org/x/text/collate/build/colelem.go
/usr/lib/golang/src/golang.org/x/text/collate/build/colelem_test.go
/usr/lib/golang/src/golang.org/x/text/collate/build/contract.go
/usr/lib/golang/src/golang.org/x/text/collate/build/contract_test.go
/usr/lib/golang/src/golang.org/x/text/collate/build/order.go
/usr/lib/golang/src/golang.org/x/text/collate/build/order_test.go
/usr/lib/golang/src/golang.org/x/text/collate/build/table.go
/usr/lib/golang/src/golang.org/x/text/collate/build/trie.go
/usr/lib/golang/src/golang.org/x/text/collate/build/trie_test.go
/usr/lib/golang/src/golang.org/x/text/collate/collate.go
/usr/lib/golang/src/golang.org/x/text/collate/collate_test.go
/usr/lib/golang/src/golang.org/x/text/collate/colltab/collate_test.go
/usr/lib/golang/src/golang.org/x/text/collate/colltab/collelem.go
/usr/lib/golang/src/golang.org/x/text/collate/colltab/collelem_test.go
/usr/lib/golang/src/golang.org/x/text/collate/colltab/colltab.go
/usr/lib/golang/src/golang.org/x/text/collate/colltab/colltab_test.go
/usr/lib/golang/src/golang.org/x/text/collate/colltab/contract.go
/usr/lib/golang/src/golang.org/x/text/collate/colltab/contract_test.go
/usr/lib/golang/src/golang.org/x/text/collate/colltab/export.go
/usr/lib/golang/src/golang.org/x/text/collate/colltab/numeric.go
/usr/lib/golang/src/golang.org/x/text/collate/colltab/numeric_test.go
/usr/lib/golang/src/golang.org/x/text/collate/colltab/table.go
/usr/lib/golang/src/golang.org/x/text/collate/colltab/trie.go
/usr/lib/golang/src/golang.org/x/text/collate/colltab/trie_test.go
/usr/lib/golang/src/golang.org/x/text/collate/export_test.go
/usr/lib/golang/src/golang.org/x/text/collate/index.go
/usr/lib/golang/src/golang.org/x/text/collate/maketables.go
/usr/lib/golang/src/golang.org/x/text/collate/option.go
/usr/lib/golang/src/golang.org/x/text/collate/option_test.go
/usr/lib/golang/src/golang.org/x/text/collate/reg_test.go
/usr/lib/golang/src/golang.org/x/text/collate/sort.go
/usr/lib/golang/src/golang.org/x/text/collate/sort_test.go
/usr/lib/golang/src/golang.org/x/text/collate/table_test.go
/usr/lib/golang/src/golang.org/x/text/collate/tables.go
/usr/lib/golang/src/golang.org/x/text/collate/tools/colcmp/chars.go
/usr/lib/golang/src/golang.org/x/text/collate/tools/colcmp/col.go
/usr/lib/golang/src/golang.org/x/text/collate/tools/colcmp/colcmp.go
/usr/lib/golang/src/golang.org/x/text/collate/tools/colcmp/darwin.go
/usr/lib/golang/src/golang.org/x/text/collate/tools/colcmp/gen.go
/usr/lib/golang/src/golang.org/x/text/collate/tools/colcmp/icu.go
/usr/lib/golang/src/golang.org/x/text/currency/common.go
/usr/lib/golang/src/golang.org/x/text/currency/currency.go
/usr/lib/golang/src/golang.org/x/text/currency/currency_test.go
/usr/lib/golang/src/golang.org/x/text/currency/gen.go
/usr/lib/golang/src/golang.org/x/text/currency/gen_common.go
/usr/lib/golang/src/golang.org/x/text/currency/tables.go
/usr/lib/golang/src/golang.org/x/text/display/dict.go
/usr/lib/golang/src/golang.org/x/text/display/dict_test.go
/usr/lib/golang/src/golang.org/x/text/display/display.go
/usr/lib/golang/src/golang.org/x/text/display/display_test.go
/usr/lib/golang/src/golang.org/x/text/display/examples_test.go
/usr/lib/golang/src/golang.org/x/text/display/lookup.go
/usr/lib/golang/src/golang.org/x/text/display/maketables.go
/usr/lib/golang/src/golang.org/x/text/display/tables.go
/usr/lib/golang/src/golang.org/x/text/doc.go
/usr/lib/golang/src/golang.org/x/text/encoding/charmap/charmap.go
/usr/lib/golang/src/golang.org/x/text/encoding/charmap/maketables.go
/usr/lib/golang/src/golang.org/x/text/encoding/charmap/tables.go
/usr/lib/golang/src/golang.org/x/text/encoding/encoding.go
/usr/lib/golang/src/golang.org/x/text/encoding/encoding_test.go
/usr/lib/golang/src/golang.org/x/text/encoding/example_test.go
/usr/lib/golang/src/golang.org/x/text/encoding/htmlindex/gen.go
/usr/lib/golang/src/golang.org/x/text/encoding/htmlindex/htmlindex.go
/usr/lib/golang/src/golang.org/x/text/encoding/htmlindex/htmlindex_test.go
/usr/lib/golang/src/golang.org/x/text/encoding/htmlindex/map.go
/usr/lib/golang/src/golang.org/x/text/encoding/htmlindex/tables.go
/usr/lib/golang/src/golang.org/x/text/encoding/ianaindex/example_test.go
/usr/lib/golang/src/golang.org/x/text/encoding/ianaindex/ianaindex.go
/usr/lib/golang/src/golang.org/x/text/encoding/internal/identifier/gen.go
/usr/lib/golang/src/golang.org/x/text/encoding/internal/identifier/identifier.go
/usr/lib/golang/src/golang.org/x/text/encoding/internal/identifier/mib.go
/usr/lib/golang/src/golang.org/x/text/encoding/internal/internal.go
/usr/lib/golang/src/golang.org/x/text/encoding/japanese/all.go
/usr/lib/golang/src/golang.org/x/text/encoding/japanese/eucjp.go
/usr/lib/golang/src/golang.org/x/text/encoding/japanese/iso2022jp.go
/usr/lib/golang/src/golang.org/x/text/encoding/japanese/maketables.go
/usr/lib/golang/src/golang.org/x/text/encoding/japanese/shiftjis.go
/usr/lib/golang/src/golang.org/x/text/encoding/japanese/tables.go
/usr/lib/golang/src/golang.org/x/text/encoding/korean/euckr.go
/usr/lib/golang/src/golang.org/x/text/encoding/korean/maketables.go
/usr/lib/golang/src/golang.org/x/text/encoding/korean/tables.go
/usr/lib/golang/src/golang.org/x/text/encoding/simplifiedchinese/all.go
/usr/lib/golang/src/golang.org/x/text/encoding/simplifiedchinese/gbk.go
/usr/lib/golang/src/golang.org/x/text/encoding/simplifiedchinese/hzgb2312.go
/usr/lib/golang/src/golang.org/x/text/encoding/simplifiedchinese/maketables.go
/usr/lib/golang/src/golang.org/x/text/encoding/simplifiedchinese/tables.go
/usr/lib/golang/src/golang.org/x/text/encoding/testdata/candide-gb18030.txt
/usr/lib/golang/src/golang.org/x/text/encoding/testdata/candide-utf-16le.txt
/usr/lib/golang/src/golang.org/x/text/encoding/testdata/candide-utf-8.txt
/usr/lib/golang/src/golang.org/x/text/encoding/testdata/candide-windows-1252.txt
/usr/lib/golang/src/golang.org/x/text/encoding/testdata/rashomon-euc-jp.txt
/usr/lib/golang/src/golang.org/x/text/encoding/testdata/rashomon-iso-2022-jp.txt
/usr/lib/golang/src/golang.org/x/text/encoding/testdata/rashomon-shift-jis.txt
/usr/lib/golang/src/golang.org/x/text/encoding/testdata/rashomon-utf-8.txt
/usr/lib/golang/src/golang.org/x/text/encoding/testdata/sunzi-bingfa-gb-levels-1-and-2-hz-gb2312.txt
/usr/lib/golang/src/golang.org/x/text/encoding/testdata/sunzi-bingfa-gb-levels-1-and-2-utf-8.txt
/usr/lib/golang/src/golang.org/x/text/encoding/testdata/sunzi-bingfa-simplified-gbk.txt
/usr/lib/golang/src/golang.org/x/text/encoding/testdata/sunzi-bingfa-simplified-utf-8.txt
/usr/lib/golang/src/golang.org/x/text/encoding/testdata/sunzi-bingfa-traditional-big5.txt
/usr/lib/golang/src/golang.org/x/text/encoding/testdata/sunzi-bingfa-traditional-utf-8.txt
/usr/lib/golang/src/golang.org/x/text/encoding/testdata/unsu-joh-eun-nal-euc-kr.txt
/usr/lib/golang/src/golang.org/x/text/encoding/testdata/unsu-joh-eun-nal-utf-8.txt
/usr/lib/golang/src/golang.org/x/text/encoding/traditionalchinese/big5.go
/usr/lib/golang/src/golang.org/x/text/encoding/traditionalchinese/maketables.go
/usr/lib/golang/src/golang.org/x/text/encoding/traditionalchinese/tables.go
/usr/lib/golang/src/golang.org/x/text/encoding/unicode/override.go
/usr/lib/golang/src/golang.org/x/text/encoding/unicode/unicode.go
/usr/lib/golang/src/golang.org/x/text/gen.go
/usr/lib/golang/src/golang.org/x/text/internal/colltab/colltab.go
/usr/lib/golang/src/golang.org/x/text/internal/colltab/colltab_test.go
/usr/lib/golang/src/golang.org/x/text/internal/colltab/contract.go
/usr/lib/golang/src/golang.org/x/text/internal/colltab/contract_test.go
/usr/lib/golang/src/golang.org/x/text/internal/colltab/iter.go
/usr/lib/golang/src/golang.org/x/text/internal/colltab/iter_test.go
/usr/lib/golang/src/golang.org/x/text/internal/gen.go
/usr/lib/golang/src/golang.org/x/text/internal/gen/code.go
/usr/lib/golang/src/golang.org/x/text/internal/gen/gen.go
/usr/lib/golang/src/golang.org/x/text/internal/gen_test.go
/usr/lib/golang/src/golang.org/x/text/internal/internal.go
/usr/lib/golang/src/golang.org/x/text/internal/match.go
/usr/lib/golang/src/golang.org/x/text/internal/match_test.go
/usr/lib/golang/src/golang.org/x/text/internal/tables.go
/usr/lib/golang/src/golang.org/x/text/internal/tag/tag.go
/usr/lib/golang/src/golang.org/x/text/internal/tag/tag_test.go
/usr/lib/golang/src/golang.org/x/text/internal/testtext/codesize.go
/usr/lib/golang/src/golang.org/x/text/internal/testtext/text.go
/usr/lib/golang/src/golang.org/x/text/internal/triegen/compact.go
/usr/lib/golang/src/golang.org/x/text/internal/triegen/data_test.go
/usr/lib/golang/src/golang.org/x/text/internal/triegen/example_compact_test.go
/usr/lib/golang/src/golang.org/x/text/internal/triegen/example_test.go
/usr/lib/golang/src/golang.org/x/text/internal/triegen/gen_test.go
/usr/lib/golang/src/golang.org/x/text/internal/triegen/print.go
/usr/lib/golang/src/golang.org/x/text/internal/triegen/triegen.go
/usr/lib/golang/src/golang.org/x/text/internal/ucd/example_test.go
/usr/lib/golang/src/golang.org/x/text/internal/ucd/ucd.go
/usr/lib/golang/src/golang.org/x/text/internal/ucd/ucd_test.go
/usr/lib/golang/src/golang.org/x/text/language/common.go
/usr/lib/golang/src/golang.org/x/text/language/coverage.go
/usr/lib/golang/src/golang.org/x/text/language/coverage_test.go
/usr/lib/golang/src/golang.org/x/text/language/data_test.go
/usr/lib/golang/src/golang.org/x/text/language/examples_test.go
/usr/lib/golang/src/golang.org/x/text/language/gen_common.go
/usr/lib/golang/src/golang.org/x/text/language/gen_index.go
/usr/lib/golang/src/golang.org/x/text/language/go1_1.go
/usr/lib/golang/src/golang.org/x/text/language/go1_2.go
/usr/lib/golang/src/golang.org/x/text/language/index.go
/usr/lib/golang/src/golang.org/x/text/language/language.go
/usr/lib/golang/src/golang.org/x/text/language/language_test.go
/usr/lib/golang/src/golang.org/x/text/language/lookup.go
/usr/lib/golang/src/golang.org/x/text/language/lookup_test.go
/usr/lib/golang/src/golang.org/x/text/language/maketables.go
/usr/lib/golang/src/golang.org/x/text/language/match.go
/usr/lib/golang/src/golang.org/x/text/language/match_test.go
/usr/lib/golang/src/golang.org/x/text/language/parse.go
/usr/lib/golang/src/golang.org/x/text/language/parse_test.go
/usr/lib/golang/src/golang.org/x/text/language/tables.go
/usr/lib/golang/src/golang.org/x/text/language/tags.go
/usr/lib/golang/src/golang.org/x/text/runes/cond.go
/usr/lib/golang/src/golang.org/x/text/runes/cond_test.go
/usr/lib/golang/src/golang.org/x/text/runes/example_test.go
/usr/lib/golang/src/golang.org/x/text/runes/runes.go
/usr/lib/golang/src/golang.org/x/text/runes/runes_test.go
/usr/lib/golang/src/golang.org/x/text/search/index.go
/usr/lib/golang/src/golang.org/x/text/search/pattern.go
/usr/lib/golang/src/golang.org/x/text/search/pattern_test.go
/usr/lib/golang/src/golang.org/x/text/search/search.go
/usr/lib/golang/src/golang.org/x/text/search/tables.go
/usr/lib/golang/src/golang.org/x/text/transform/examples_test.go
/usr/lib/golang/src/golang.org/x/text/transform/transform.go
/usr/lib/golang/src/golang.org/x/text/transform/transform_test.go
/usr/lib/golang/src/golang.org/x/text/unicode/norm/composition.go
/usr/lib/golang/src/golang.org/x/text/unicode/norm/composition_test.go
/usr/lib/golang/src/golang.org/x/text/unicode/norm/example_iter_test.go
/usr/lib/golang/src/golang.org/x/text/unicode/norm/forminfo.go
/usr/lib/golang/src/golang.org/x/text/unicode/norm/forminfo_test.go
/usr/lib/golang/src/golang.org/x/text/unicode/norm/input.go
/usr/lib/golang/src/golang.org/x/text/unicode/norm/iter.go
/usr/lib/golang/src/golang.org/x/text/unicode/norm/iter_test.go
/usr/lib/golang/src/golang.org/x/text/unicode/norm/maketables.go
/usr/lib/golang/src/golang.org/x/text/unicode/norm/norm_test.go
/usr/lib/golang/src/golang.org/x/text/unicode/norm/normalize.go
/usr/lib/golang/src/golang.org/x/text/unicode/norm/normalize_test.go
/usr/lib/golang/src/golang.org/x/text/unicode/norm/readwriter.go
/usr/lib/golang/src/golang.org/x/text/unicode/norm/readwriter_test.go
/usr/lib/golang/src/golang.org/x/text/unicode/norm/tables.go
/usr/lib/golang/src/golang.org/x/text/unicode/norm/transform.go
/usr/lib/golang/src/golang.org/x/text/unicode/norm/transform_test.go
/usr/lib/golang/src/golang.org/x/text/unicode/norm/trie.go
/usr/lib/golang/src/golang.org/x/text/unicode/norm/triegen.go
/usr/lib/golang/src/golang.org/x/text/unicode/norm/ucd_test.go
/usr/lib/golang/src/golang.org/x/text/unicode/rangetable/gen.go
/usr/lib/golang/src/golang.org/x/text/unicode/rangetable/merge.go
/usr/lib/golang/src/golang.org/x/text/unicode/rangetable/merge_test.go
/usr/lib/golang/src/golang.org/x/text/unicode/rangetable/rangetable.go
/usr/lib/golang/src/golang.org/x/text/unicode/rangetable/rangetable_test.go
/usr/lib/golang/src/golang.org/x/text/unicode/rangetable/tables.go
/usr/lib/golang/src/golang.org/x/text/width/common_test.go
/usr/lib/golang/src/golang.org/x/text/width/example_test.go
/usr/lib/golang/src/golang.org/x/text/width/gen.go
/usr/lib/golang/src/golang.org/x/text/width/gen_common.go
/usr/lib/golang/src/golang.org/x/text/width/gen_trieval.go
/usr/lib/golang/src/golang.org/x/text/width/kind_string.go
/usr/lib/golang/src/golang.org/x/text/width/runes_test.go
/usr/lib/golang/src/golang.org/x/text/width/tables.go
/usr/lib/golang/src/golang.org/x/text/width/tables_test.go
/usr/lib/golang/src/golang.org/x/text/width/transform.go
/usr/lib/golang/src/golang.org/x/text/width/transform_test.go
/usr/lib/golang/src/golang.org/x/text/width/trieval.go
/usr/lib/golang/src/golang.org/x/text/width/width.go
