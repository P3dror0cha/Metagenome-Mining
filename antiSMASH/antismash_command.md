    antismash "$arquivo" \
        --genefinding-tool prodigal \
        --cb-general \
        --cb-knownclusters \
        --cb-subclusters \
        --asf \
        --pfam2go \
        --tigrfam \
        --output-dir "$output_dir/$nome"

Parâmetros:

--genefinding-tool = Preditor de ORF usado pelo antiSMASH.

--cb-general = Compara clusters com a base de dados do próprio antiSMASH (ClusterBlast: shows regions from the antiSMASH Database that are similar to the current region)

--cb-knownclusters = Compara clusters com o MIBIG Database (KnownClusterBlast: shows clusters from MIBiG that are similar to the current region)

--cb-subclusters = SubClusterBlast: shows sub-cluster units related to the current region

--asf = Verifica sítios ativos de proteínas importantes e reporta modificações.

--pfam2go = Compara os CDS dos BGCs com a base de dados do PFAM (famílias e domínios proteicos)

--tigrfam = Compara os CDS dos BGCs com a base de dados do Tigrfam

--output-dir = Diretório de saída
