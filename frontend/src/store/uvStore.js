import { reactive } from "vue"

export const uvStore = reactive({
  uv: null,
  location: "Australia",
  level: "",
  uvColor: "#f1c40f",
  markerPosition: "20%",
  fetched: false,
})
