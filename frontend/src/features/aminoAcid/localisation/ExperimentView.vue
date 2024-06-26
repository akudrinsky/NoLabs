<template>
  <div v-if="experimentLoaded">
    <q-separator></q-separator>
    <q-layout container style="height: 100vh">
      <ExperimentHeader :experiment-name="experiment?.name" :on-experiment-name-change-submit="onExperimentNameChange">
        <q-btn color="info" size="md" outline label="Localisation parameters"
               @click="showInferenceForm = !showInferenceForm"/>
      </ExperimentHeader>
      <q-page-container>
        <div class="row" v-if="experimentHasGeneratedData">
          <div class="col-6">
            <div class="q-ma-sm">
              <AminoAcidTable :on-amino-acid-open="setActiveAminoAcid" :rows="experiment?.aminoAcids"/>
            </div>
          </div>
          <div class="col-2">
            <div class="q-ma-sm">
              <q-toolbar class="bg-primary text-white shadow-2">
                <q-toolbar-title>Probabilities</q-toolbar-title>
              </q-toolbar>
              <q-list bordered separator>
                <q-item clickable v-ripple v-for="data in listItemData"
                        @mouseenter="setActiveListItem(data.key)"
                        @mouseleave="resetActiveListItem" :key="data.key">
                  <q-item-section>
                    {{ data.text }}
                  </q-item-section>
                </q-item>
              </q-list>
            </div>
          </div>
          <div class="col-4">
            <div class="q-pl-sm q-ma-sm">
              <q-img
                  :src="activeImage"
                  style="height: 500px; max-width: 500px;"
              />
            </div>
          </div>
        </div>
      </q-page-container>
    </q-layout>
    <q-dialog v-model="showInferenceForm" position="right" :maximized="true">
      <q-card>
        <q-card-section class="row items-center q-pb-none">
          <div class="text-h6">Localisation parameters</div>
          <q-space/>
          <q-btn icon="close" flat round dense v-close-popup/>
        </q-card-section>
        <q-card-section>
          <AminoAcidInferenceForm :on-submit="onSubmit" :properties="experiment?.properties"/>
        </q-card-section>
      </q-card>
    </q-dialog>
  </div>
</template>

<script lang="ts">
import {defineComponent, ref} from 'vue'
import {QVueGlobals, QSpinnerOrbit} from 'quasar';
import ExperimentHeader from "src/components/ExperimentHeader.vue";
import useLocalisationStore from "src/features/aminoAcid/localisation/storage";
import {AminoAcid} from "src/features/aminoAcid/localisation/types";
import {Experiment} from "src/features/aminoAcid/types";
import AminoAcidInferenceForm from "src/features/aminoAcid/AminoAcidInferenceForm.vue";
import AminoAcidTable from "src/features/aminoAcid/AminoAcidTable.vue";


export default defineComponent({
  name: 'LocalisationExperimentView',
  data() {
    const store = useLocalisationStore();

    const images: { [key: string]: string } = {
      mitochondria: '/localisationImages/mithochondria.png',
      nucleus: '/localisationImages/nucleus.png',
      cytoplasm: '/localisationImages/cytoplasm.png',
      extracellular: '/localisationImages/original.png',
      other: '/localisationImages/original.png',
      original: '/localisationImages/original.png',
    };

    return {
      experiment: null as Experiment<AminoAcid>,
      showInferenceForm: false,
      store,
      activeImage: images.original,
      listItemData: [] as Array<{
        key: string,
        text: string,
        image: string
      }>,
      images
    }
  },
  computed: {
    experimentLoaded(): boolean {
      return this.experiment !== null;
    },
    experimentHasGeneratedData(): boolean {
      return this.experimentLoaded && this.experiment!.aminoAcids.length > 0;
    },
    aminoAcidRows() {
      return this.experiment?.aminoAcids;
    },
  },
  methods: {
    setActiveAminoAcid(aminoAcidName: string): void {
      const aminoAcid = this.experiment?.aminoAcids.find(x => x.name === aminoAcidName);
      this.listItemData = [
        {
          key: 'mitochondria',
          text: `Mitochondria ${this.formatText(aminoAcid?.mitochondialProteins!)}`,
          image: this.images.mitochondria
        },
        {
          key: 'nucleus',
          text: `Nucleus  ${this.formatText(aminoAcid?.nuclearProteins!)}`,
          image: this.images.nucleus
        },
        {
          key: 'cytoplasm',
          text: `Cytoplasm ${this.formatText(aminoAcid?.cytosolicProteins!)}`,
          image: this.images.cytoplasm
        },
        {
          key: 'extracellular',
          text: `Extracellular ${this.formatText(aminoAcid?.extracellularSecretedProteins!)}`,
          image: this.images.original
        },
        {
          key: 'other',
          text: `Other ${this.formatText(aminoAcid?.otherProteins!)}`,
          image: this.images.other
        }
      ]
      this.activeImage = this.images.original;
    },
    setExperiment(experiment: Experiment<AminoAcid> | null){
      if (experiment !== null) {
        this.experiment = experiment;

        if(experiment.aminoAcids.length > 0){
          this.setActiveAminoAcid(experiment.aminoAcids[0]!.name);
        }
      }
    },
    setActiveListItem(key: string) {
      this.activeImage = this.listItemData.find(x => x.key === key)!.image;
    },
    resetActiveListItem() {
      this.activeImage = this.images.original;
    },
    formatText(prob: number): number {
      return (prob as any).toFixed(6) * 100;
    },
    async onExperimentNameChange(newExperimentName: string) {
      await this.store.changeExperimentName(this.experiment?.id as string, newExperimentName);
      this.experiment!.name = newExperimentName;
    },
    async onSubmit(data: { aminoAcidSequence: string, fastas: Array<File> }) {
      this.$q.loading.show({
        spinner: QSpinnerOrbit,
        message: 'Running AI models. This can take a couple of minutes'
      });

      const response = await this.store.inference({
        experimentId: this.experiment!.id,
        experimentName: this.experiment!.name,
        aminoAcidSequence: data.aminoAcidSequence,
        fastas: data.fastas
      });

      this.setExperiment(response.experiment);

      this.showInferenceForm = false;

      this.$q.loading.hide();
    },
  },
  async mounted() {
    const experimentId = this.$route.params.experimentId as string;

    this.$q.loading.show({
      spinner: QSpinnerOrbit,
      message: `Experiment ${experimentId}`
    });

    const response = await this.store.getExperiment(experimentId);

    this.setExperiment(response.experiment);

    this.$q.loading.hide();

    if (!this.experimentHasGeneratedData) {
      this.showInferenceForm = true;
    }
  },
  components: {
    AminoAcidTable,
    ExperimentHeader,
    AminoAcidInferenceForm
  }
})
</script>
  