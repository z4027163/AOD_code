#!/bin/bash

if [ "$1" == "" ] || [ "$2" == "" ] || [ "$4" == "" ] || [ "$4" == "" ]; then
    echo "Please provide arguments to the script: site configuration, data type and MC type"
    echo "Usage bash loopcheck_bkg_<finalstate>.sh <arg1> <arg2> <arg3> <arg4>"
    exit      
fi


echo "$1 configuration";
echo "$2 data"
echo "$3 simulation"

SCERN="CERN";
SFNAL="FNAL";
SDESY="DESY";
SBARI="BARI";

###### Background
n=0;
m=0;

mkdir -p jobs$4;

echo "Reading bkg_input_$3_AN.txt file"

cp -f bkg_input_$3_AN.txt bkg_input.txt
nlines=`wc -l bkg_input_$3_AN.txt | awk '{print $1}'`;

mkdir -p BkgCards$4$3;

while [ $n -lt ${nlines} ]; do
  (( n = n + 1 ))
  (( m = ${nlines} - n ))
  echo $n $m
  rm -f BkgCards$4$3/bkg_input_${n}.txt
  head -1 bkg_input.txt  > BkgCards$4$3/bkg_input_${n}.txt
  samplename=`cat BkgCards$4$3/bkg_input_${n}.txt | awk '{print $1}'`
  echo $samplename
  tail -n $m bkg_input.txt >  bkg_input_tmp.txt
  mv  bkg_input_tmp.txt bkg_input.txt
  rm -f jobs$4/submit_ReferenceAnalysis_bkg_${samplename}_$4.sh
  if [ $1 = ${SCERN} ]; then
      cat submit_HZZ4LeptonsAnalysis_CERN.sh | sed "s?site?$1?g" | sed "s?mc?$3?g" |sed "s?year?$2?g" | sed "s?HZZ4LeptonsAnalysis?RunReferenceAnalysis?g" | sed "s?jobdir?jobs$4_25ns?g" | sed "s?histodir?histos$4_25ns?g" | sed "s?output?output_${samplename}?g" | sed "s?RunReferenceAnalysis?RunReference4mu_bkg?g" | sed "s?bkg_input.txt?BkgCards4mu$3/bkg_input_${n}.txt?g" | sed "s?_log?_${samplename}_$4.log?g" > jobs4mu/submit_ReferenceAnalysis_bkg_${samplename}_4mu.sh
  elif  [ $1 = ${SFNAL} ]; then 
      cat submit_HZZ4LeptonsAnalysis_FNAL.sh | sed "s?site?$1?g" | sed "s?mc?$3?g" |sed "s?year?$2?g" | sed "s?HZZ4LeptonsAnalysis?RunReferenceAnalysis?g" | sed "s?jobdir?jobs4mu_25ns?g" | sed "s?histodir?histos4mu_25ns?g" | sed "s?output?output_${samplename}?g" | sed "s?RunReferenceAnalysis?RunReference4mu_bkg?g" | sed "s?bkg_input.txt?BkgCards4mu$3/bkg_input_${n}.txt?g" | sed "s?_log?_${samplename}_4mu.log?g" > jobs4mu/submit_ReferenceAnalysis_bkg_${samplename}_4mu.sh
      cat condor_template.cfg  | sed "s?submit_HZZ4LeptonsAnalysis_FNAL?submit_ReferenceAnalysis_bkg_${samplename}_4mu?g" | sed "s?RunReferenceAnalysis?RunReference4mu_bkg?g" | sed "s?sig_input_h150.txt?BkgCards4mu$3/bkg_input_${n}.txt?g" | sed "s?mail?`whoami`?g" > jobs4mu/condor_ReferenceAnalysis_bkg_${samplename}_4mu.cfg      
  elif  [ $1 = ${SDESY} ]; then
     cat submit_HZZ4LeptonsAnalysis_DESY.sh | sed "s?site?$1?g" | sed "s?mc?$3?g" |sed "s?year?$2?g" | sed "s?HZZ4LeptonsAnalysis?RunReferenceAnalysis?g" | sed "s?jobdir?jobs4mu_25ns?g" | sed "s?histodir?histos4mu_25ns?g" | sed "s?output?output_${samplename}?g" | sed "s?RunReferenceAnalysis?RunReference4mu_bkg?g" | sed "s?bkg_input.txt?BkgCards4mu$3/bkg_input_${n}.txt?g" | sed "s?_log?_${samplename}_4mu.log?g" > jobs4mu/submit_ReferenceAnalysis_bkg_${samplename}_4mu.sh
  elif  [ $1 = ${SBARI} ]; then
      cat submit_HZZ4LeptonsAnalysis_BARI.sh | sed "s?CMSSW_BASE_DIR?${CMSSW_BASE}?g" | sed "s?path?$PATH?g"  | sed "s?lib:?$LD_LIBRARY_PATH:?g" | sed "s?4mu?$4?g" | sed "s?mc?$3?g" |sed "s?year?$2?g" | sed "s?HZZ4LeptonsAnalysis?RunReferenceAnalysis_bkg?g" | sed "s?jobdir?jobs$4_25ns?g" | sed "s?histodir?histos$4_25ns?g" | sed "s?output?output_${samplename}?g" | sed "s?RunReferenceAnalysis?RunReference$4_bkg?g" | sed "s?bkg_input.txt?bkg_input_${n}.txt?g" | sed "s?_log?_${samplename}_$4.log?g" > jobs$4/submit_ReferenceAnalysis_bkg_${samplename}_$4.sh
      cat condor_template.cfg  | sed "s?4mu?$4?g" | sed "s?submit_HZZ4LeptonsAnalysis_BARI?submit_ReferenceAnalysis_bkg_${samplename}_$4?g" | sed "s?RunReferenceAnalysis?RunReference$4_bkg?g" | sed "s?sig_input_h150.txt?BkgCards$4$3/bkg_input_${n}.txt?g" | sed "s?mail?`whoami`?g" > jobs$4/condor_ReferenceAnalysis_bkg_${samplename}_$4.cfg
  else
      cat submit_HZZ4LeptonsAnalysis.sh | sed "s?mc?$3?g" |sed "s?year?$2?g" | sed "s?HZZ4LeptonsAnalysis?RunReferenceAnalysis_bkg?g" | sed "s?jobdir?jobs4mu_25ns?g" | sed "s?histodir?histos4mu_25ns?g" | sed "s?output?output_${samplename}?g" | sed "s?RunReferenceAnalysis?RunReference4mu_bkg?g" | sed "s?bkg_input.txt?BkgCards4mu$3/bkg_input_${n}.txt?g" | sed "s?_log?_${samplename}_4mu.log?g" > jobs4mu/submit_ReferenceAnalysis_bkg_${samplename}_4mu.sh

  fi

  chmod u+xr jobs$4/submit_ReferenceAnalysis_bkg_${samplename}_$4.sh

  cd jobs$4

  if [ $1 = ${SCERN} ]; then
      echo "Submitting jobs via LSF at CERN"
      bsub -q 8nh  submit_ReferenceAnalysis_bkg_${samplename}_4mu.sh
  elif  [ $1 = ${SFNAL} ]; then
      echo "Submitting jobs via CONDOR at FNAL"
      condor_submit  condor_ReferenceAnalysis_bkg_${samplename}_4mu.cfg
  elif  [ $1 = ${SDESY} ]; then
      echo "Submitting jobs via SGE"
      qsub submit_ReferenceAnalysis_bkg_${samplename}_4mu.sh   
  elif  [ $1 = ${SBARI} ]; then
      echo "Submitting jobs via CONDOR at BARI"
      condor_submit -name ettore  condor_ReferenceAnalysis_bkg_${samplename}_$4.cfg
  else
      echo "Submitting jobs via PBS"    
      qsub -q local submit_ReferenceAnalysis_bkg_${samplename}_4mu.sh
  fi
  cd ..
done 
