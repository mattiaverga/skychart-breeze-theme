# A script to generate png icons from svgs
# Probably not the best, but it does the work
# It needs Inkscape installed on the system

import os

currDir = os.path.dirname(os.path.realpath(__file__))
pngDir = currDir + os.sep + "icons"

with open('corrispondenze.txt', 'r') as indexFile :
        for line in indexFile :
                record = line.split('\t')
                
                for style in ("daylight","night-vision") :
                        for svgSize in ("16","22") :
                                svgFile = os.path.join(currDir, 'svg', style, svgSize+'x'+svgSize, record[1].strip() + ".svg")
                                #Check files existence
                                if not os.path.isfile(svgFile) :
                                        print(svgFile + " not found")
                                        sys.exit()
                                #Use 16px SVGs only for 16px icons and 22px SVGs for upscale
                                if svgSize == "22" :
                                        for pngSize in ("22","32","64") :
                                                #Check png directory existence
                                                if not os.path.exists(os.path.join(pngDir, style, pngSize+"x"+pngSize)) :
                                                        os.makedirs(os.path.join(pngDir, style, pngSize+"x"+pngSize))
                                                pngFile = os.path.join(pngDir, style, pngSize+"x"+pngSize, record[0].strip() + ".png")
                                                # Create icon only if not existent
                                                if not os.path.isfile(pngFile):
                                                    os.system("inkscape -z -f \"" + svgFile +"\" -w " + pngSize + " -e \"" + pngFile + "\"")
                                else :
                                        #Check png directory existence
                                        if not os.path.exists(os.path.join(pngDir, style, svgSize+"x"+svgSize)) :
                                                os.makedirs(os.path.join(pngDir, style, svgSize+"x"+svgSize))
                                        pngFile = os.path.join(pngDir, style, svgSize+"x"+svgSize, record[0].strip() + ".png")
                                        # Create icon only if not existent
                                        if not os.path.isfile(pngFile):
                                            os.system("inkscape -z -f \"" + svgFile +"\" -w " + svgSize + " -e \"" + pngFile + "\"")
