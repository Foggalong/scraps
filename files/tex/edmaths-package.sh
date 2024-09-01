#!/usr/bin/env bash

# packaging script for the `edmaths` and `beamertheme-edmaths packages
VERSION="0.99"


echo "Deleting any residual packging directories..."

if [ -d "edmaths/" ]; then
    rm -r "edmaths/"
fi

if [ -d "beamertheme-edmaths/" ]; then
    rm -r "beamertheme-edmaths/"
fi


EDMATHS_README=$(cat << EOM
# \`edmaths\` Report & Thesis Class

A report and thesis stylesheet for easier compliance with the [university's typesetting rules](https://www.ed.ac.uk/academic-services/students/thesis-submission). See also the [_documentation_](https://foggalong.github.io/edinburgh-math-latex/edmaths-docs.pdf) and a [_compiled example_](https://foggalong.github.io/edinburgh-math-latex/example-report.pdf). To use, place the files and store them either with your .tex file(s) or in any directory that's findable by LaTeX (e.g. \`\$TEXINPUTS\`).

For more information on the wider project, including the beamer theme, [see GitHub](https://github.com/Foggalong/edinburgh-math-latex). The stylesheet [edmaths.sty](edmaths.sty) is provided under the [LaTeX Project Public License v1.3c](https://choosealicense.com/licenses/lppl-1.3c/) (LPPL) while the example [example-report.tex](example-report.tex) is provided under the [BSD Zero Clause License](https://choosealicense.com/licenses/0bsd/) (0BSD).
EOM
)

BEAMER_README=$(cat << EOM
# \`beamertheme-edmaths\` Beamer Theme

A beamer presentation theme which follows the [university's brand guidelines](https://communications-marketing.ed.ac.uk/marketing/brand). See also the [_documentation_](https://foggalong.github.io/edinburgh-math-latex/beamertheme-edmaths-docs.pdf) and a [_compiled example_](https://foggalong.github.io/edinburgh-math-latex/example-presentation.pdf). To use, place the files and store them either with your .tex file(s) or in any directory that's findable by LaTeX (e.g. \`\$TEXINPUTS\`).

For more information on the wider project, including the report and thesis stylesheet, [see GitHub](https://github.com/Foggalong/edinburgh-math-latex). The beamer theme [beamerthemeedmaths.sty](beamerthemeedmaths.sty) is provided under the [LaTeX Project Public License v1.3c](https://choosealicense.com/licenses/lppl-1.3c/) (LPPL) while the example [example-presentation.tex](example-presentation.tex) is provided under the [BSD Zero Clause License](https://choosealicense.com/licenses/0bsd/) (0BSD).
EOM
)


echo "Collating files for edmaths..."
# base structure
mkdir edmaths/
echo -e "$EDMATHS_README" | tee edmaths/README.md
cp main/LICENSE.txt edmaths/
# stylesheet files
cp main/edmaths.sty edmaths/
cp main/example-references.bib edmaths/
cp main/example-report.tex edmaths/
# documentation
mkdir edmaths/docs/
cp main/docs/edmaths-docs.tex edmaths/docs/
if [ ! -f "main/docs/edmaths-docs.pdf" ]; then
    echo "Compiling documentation..."
    cd main/docs/ || (echo "Directory error!" && exit)
    pdflatex edmaths-docs.tex
    cd ../../
fi
cp main/docs/edmaths-docs.pdf edmaths/docs/

echo "Creating ZIP file..."
zip -r edmaths-$VERSION.zip edmaths/


echo "Collating files for beamertheme-edmaths..."
# base structure
mkdir beamertheme-edmaths/
echo -e "$BEAMER_README" | tee beamertheme-edmaths/README.md
cp main/LICENSE.txt beamertheme-edmaths/
# stylesheet files
cp main/beamerthemeedmaths.sty beamertheme-edmaths/
cp main/example-references.bib beamertheme-edmaths/
cp main/example-presentation.tex beamertheme-edmaths/
cp -r main/images beamertheme-edmaths/ 
# documentation
mkdir beamertheme-edmaths/docs/
cp main/docs/beamertheme-edmaths-docs.tex beamertheme-edmaths/docs/
cp main/docs/pdfpc-screenshot.png beamertheme-edmaths/docs/
if [ ! -f "main/docs/beamertheme-edmaths-docs.pdf" ]; then
    echo "Compiling documentation..."
    cd main/docs/ || (echo "Directory error!" && exit)
    pdflatex beamertheme-edmaths-docs.tex
    cd ../../
fi
cp main/docs/beamertheme-edmaths-docs.pdf beamertheme-edmaths/docs/

echo "Creating ZIP file..."
zip -r beamertheme-edmaths-$VERSION.zip beamertheme-edmaths/


echo "Delete packaging directories?"
read -rp "$* [y/n]: " yn
case $yn in
    [Yy]*) rm -r beamertheme-edmaths/ edmaths/  ;;  
    [Nn]*) pass ;;
esac

echo "Done!"
