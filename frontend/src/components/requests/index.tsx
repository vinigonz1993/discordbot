import axios from 'axios';

const baseURLOCTranspo = `${process.env.REACT_API}/oct`;

export default {
    oct: {
        get: () => axios.get(
            baseURLOCTranspo,
            {
                method: 'GET',
                params: {
                    stopNo: 1222,
                    routeNo: 57
                },
            },
        ),
    },
};