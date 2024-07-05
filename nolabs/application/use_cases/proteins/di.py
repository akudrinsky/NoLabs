from nolabs.application.use_cases.proteins.use_cases import SearchProteinsContentFeature, GetProteinFeature, \
    DeleteProteinFeature, UploadProteinFeature, UpdateProteinFeature, GetProteinMetadataFeature, \
    SearchProteinsMetadataFeature


class ProteinsControllerDependencies:
    @staticmethod
    def search_proteins_content() -> SearchProteinsContentFeature:
        return SearchProteinsContentFeature()

    @staticmethod
    def search_proteins_metadata() -> SearchProteinsMetadataFeature:
        return SearchProteinsMetadataFeature()

    @staticmethod
    def get_protein() -> GetProteinFeature:
        return GetProteinFeature()

    @staticmethod
    def get_protein_metadata() -> GetProteinMetadataFeature:
        return GetProteinMetadataFeature()

    @staticmethod
    def upload_protein() -> UploadProteinFeature:
        return UploadProteinFeature()

    @staticmethod
    def delete_protein() -> DeleteProteinFeature:
        return DeleteProteinFeature()

    @staticmethod
    def update_protein() -> UpdateProteinFeature:
        return UpdateProteinFeature()