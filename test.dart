
Future<void> updateFavori(
  String nom,
  bool favori,
  String table,  
) async {

  if (table == 'restaurants') {
    await RestaurantsTable().update(
      data: {
        'favori': favori,
      },
      matchingRows: (rows) => rows.eqOrNull(
        'nom',
        nom,
      ),
      returnRows: false,
    );
  } else if (table == 'bars') {
    await BarsTable().update(
      data: {
        'favori': favori,
      },
      matchingRows: (rows) => rows.eqOrNull(
        'nom',
        nom,
      ),
      returnRows: false,
    );
  } else if (table == 'loisirs') {
    await LoisirsTable().update(
      data: {
        'favori': favori,
      },
      matchingRows: (rows) => rows.eqOrNull(
        'nom',
        nom,
      ),
      returnRows: false,
    );
  } else if (table == 'aemporter') {
    await AEmporterTable().update(
      data: {
        'favori': favori,
      },
      matchingRows: (rows) => rows.eqOrNull(
        'nom',
        nom,
      ),
      returnRows: false,
    );
  } else if (table == 'micro-brasseries') {
    await MicroBrasseriesTable().update(
      data: {
        'favori': favori,
      },
      matchingRows: (rows) => rows.eqOrNull(
        'nom',
        nom,
      ),
      returnRows: false,
    );
  } else if (table == 'guinguettes') {
    await GuinguettesTable().update(
      data: {
        'favori': favori,
      },
      matchingRows: (rows) => rows.eqOrNull(
        'nom',
        nom,
      ),
      returnRows: false,
    );
  } else if (table == 'avisiter') {
    await LieuxTable().update(
      data: {
        'favori': favori,
      },
      matchingRows: (rows) => rows.eqOrNull(
        'nom',
        nom,
      ),
      returnRows: false,
    );
  }
}
