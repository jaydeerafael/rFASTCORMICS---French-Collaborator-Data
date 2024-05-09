% Load cobratoolbox
addpath(genpath('/Users/jaydee/cobratoolbox')) % Change to your path 
initCobraToolbox(false)

% discretize
discretized = discretize_FPKM(fpkm, colnames)

% Load Recon3D, FASTCC, and other inputs
load('recon3d path') % Change to your path 
model = Recon3DModel
A = fastcc_4_rfastcormics(model, 1e-4,0) % create consistent model by running FASTCC (Vlassis et al., 2014)
Cmodel = removeRxns(model, model.rxns(setdiff(1:numel(model.rxns),A)))
load dico_rFASTCORMICS.mat % dictionary to map the rownname identifier to the genes in the model
biomass_rxn = {'biomass_maintenance'} % biomass is called "biomass_maintenance" in Recon3D
already_mapped_tag = 0;
epsilon = 1e-4; % avoid small number errors
consensus_proportion = 0.9;


% Optional settings included in the example

unpenalizedSystems = {'Transport, endoplasmic reticular';
    'Transport, extracellular';
    'Transport, golgi apparatus';
    'Transport, mitochondrial';
    'Transport, peroxisomal';
    'Transport, lysosomal';
    'Transport, nuclear'};
unpenalized = Cmodel.rxns(ismember(Cmodel.subSystems,unpenalizedSystems));

optional_settings.unpenalized = unpenalized;
optional_settings.func = {'biomass_maintenance','DM_atp_c_'}; % forced additional reactions into the  model
not_medium_constrained = 'EX_tag_hs(e)';
optional_settings.not_medium_constrained = not_medium_constrained;



% Create models
for i = 1:numel(colnames) %for each sample
    [model_out{i}, A_keep{i}] = fastcormics_RNAseq(Cmodel, discretized(:,i), rownames, dico, ...
        biomass_rxn, already_mapped_tag, consensus_proportion, epsilon, optional_settings);
end


% Run FBA

% Number of models in model_out
numModels = numel(model_out);

% Initialize an empty cell array to store FBA scores
FBAscores = cell(numModels, 1);

% Loop through each model and perform FBA
for i = 1:numModels
result = optimizeCbModel(model_out{i});
FBAscores{i} = result;
end

