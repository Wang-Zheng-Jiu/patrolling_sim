#!/usr/bin/env python
#
# GIT version. Please do not edit this file.
# Make a copy and edit the copy.
#
# Maps: grid, example, cumberland, DISlabs
# Alg: RAND,CR,HCR,HPCC,CGG,MSP,GBS,SEBS,DTAG,DTAS
# Loc mode: odom, GPS
# Term: gnome-terminal,xterm


import sys, time, os

MAP='DISlabs'
NROBOTS=4
MACHINE='iocchi-vm-ROSGroovy'
vALG=['SEBS', 'DTAG']  # algorithms to compare

tarstr=''

def plot_ALG(MAP,NROBOTS,vALG,MACHINE,EXT):
  global tarstr
  outfile = '%s_%d/%s_%d.png' %(MAP,NROBOTS,MAP,NROBOTS)
  # plot string
  pstr="plot "
  for i in range(0,len(vALG)):
    a = vALG[i]
    sdir = "%s_%s/%s/%s/" %(MAP, NROBOTS, a, MACHINE)
    v = findAll(sdir,EXT)
    for i in range(0,len(v)):
      s = "'%s%s' w li title '%s %s', " % (sdir,v[i],a,v[i])
      pstr = pstr + s
  pstr = pstr[0:-2]
  scmd = "gnuplot -e \"set terminal png; set output '%s'; %s\"" %(outfile, pstr)
  #print scmd
  os.system(scmd)
  print "Plot: %s" %(outfile)
  tarstr = tarstr+' '+outfile
  os.system('display '+outfile)


def plot(MAP,NROBOTS,ALG,MACHINE,EXT):
  global tarstr
  sdir = "%s_%s/%s/%s/" %(MAP, NROBOTS, ALG, MACHINE)  
  v = findAll(sdir,EXT)
  
  #if (len(VIN)==1):
  #  outfile = sdir+VIN[0]+'.png'
  #else:
  outfile = sdir+'%s_%d_%s_%s.png' % (MAP,NROBOTS,ALG,EXT[1:])
  # plot string
  pstr="plot "
  for i in range(0,len(v)):
    #s = "'%s%s' w li title '%s %d', " % (sdir,v[i],ALG,(i+1))
    s = "'%s%s' w li title '%s', " % (sdir,v[i],v[i])
    pstr = pstr + s
  pstr = pstr[0:-2]
  scmd = "gnuplot -e \"set terminal png; set output '%s'; %s\"" %(outfile, pstr)
  #print scmd
  os.system(scmd)
  print "Plot: %s" %(outfile)
  tarstr = tarstr+' '+outfile
  os.system('display '+outfile)

# returns vector of all files in the dir with this ext
def findAll(sdir,ext):
  v=[]
  i=0
  for file in os.listdir(sdir):
    if file.endswith(ext):
      v.append(file)
      i=i+1
  v.sort()
  return v

if __name__ == '__main__':

  # To generate a tar file with all the plots
  tarstr = 'tar czvf %s_%d.tgz ' %(MAP,NROBOTS)

  # Plot the comparison histogram
  plot_ALG(MAP,NROBOTS,vALG,MACHINE,".chist")

  # Plot the single histograms
  for i in range(0,len(vALG)):
    a = vALG[i]
    plot(MAP,NROBOTS,a,MACHINE,".hist")
    plot(MAP,NROBOTS,a,MACHINE,".chist")

  # Create a tgz file with all the plot images
  print tarstr
  os.system(tarstr)


#    if (len(sys.argv)<3):
#        sys.exit(0)
#    mapname = sys.argv[1]
#    vip = sys.argv[2]

