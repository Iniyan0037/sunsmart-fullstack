import { createRouter, createWebHistory } from "vue-router";

// Main pages
import HomeView from "../views/HomeView.vue";
import UVTrackerView from "../views/UVTrackerView.vue";
import UVAdviceView from "../views/UVAdviceView.vue";

// UV Advice detail
import LowAdviceView from "../views/LowAdviceView.vue";
import ModerateAdviceView from "../views/ModerateAdviceView.vue";
import HighAdviceView from "../views/HighAdviceView.vue";
import VeryHighAdviceView from "../views/VeryHighAdviceView.vue";
import ExtremeAdviceView from "../views/ExtremeAdviceView.vue";

// Skin
import SkinTypeView from "../views/SkinTypeView.vue";
import SkinType1View from "../views/SkinType1View.vue";
import SkinType2View from "../views/SkinType2View.vue";
import SkinType3View from "../views/SkinType3View.vue";
import SKinType4View from "../views/SKinType4View.vue";
import SkinType5View from "../views/SkinType5View.vue";

// Learn / Resources
import ResourcesView from "../views/ResourcesView.vue";
import UVTypesView from "../views/UVTypesView.vue";
import VitaminDView from "../views/VitaminDView.vue";
import SkinCancerView from "../views/SkinCancerView.vue";

// Research
import SkinCancerResearchView from "../views/SkinCancerResearchView.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/uv",
    name: "uv",
    component: UVTrackerView,
  },
  {
    path: "/uv-advice",
    name: "uv-advice",
    component: UVAdviceView,
  },
  {
    path: "/uv-advice/low",
    name: "low",
    component: LowAdviceView,
  },
  {
    path: "/uv-advice/moderate",
    name: "moderate",
    component: ModerateAdviceView,
  },
  {
    path: "/uv-advice/high",
    name: "high",
    component: HighAdviceView,
  },
  {
    path: "/uv-advice/veryhigh",
    name: "veryhigh",
    component: VeryHighAdviceView,
  },
  {
    path: "/uv-advice/extreme",
    name: "extreme",
    component: ExtremeAdviceView,
  },
  {
    path: "/skin",
    name: "skin",
    component: SkinTypeView,
  },
  {
    path: "/skin/type1",
    name: "skin-type1",
    component: SkinType1View,
  },
  {
    path: "/skin/type2",
    name: "skin-type2",
    component: SkinType2View,
  },
  {
    path: "/skin/type3",
    name: "skin-type3",
    component: SkinType3View,
  },
  {
    path: "/skin/type4",
    name: "skin-type4",
    component: SKinType4View,
  },
  {
    path: "/skin/type5",
    name: "skin-type5",
    component: SkinType5View,
  },
  {
    path: "/resources",
    name: "resources",
    component: ResourcesView,
  },
  {
    path: "/learn/uv",
    name: "uv-types",
    component: UVTypesView,
  },
  {
    path: "/learn/vitamind",
    name: "vitamin-d",
    component: VitaminDView,
  },
  {
    path: "/learn/skincancer",
    name: "skin-cancer",
    component: SkinCancerView,
  },
  {
    path: "/research",
    name: "research",
    component: SkinCancerResearchView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
