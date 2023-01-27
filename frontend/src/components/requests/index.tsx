import axios from 'axios';

const apiOCTranspo = axios.create({
    baseURL: `${process.env.REACT_API}`,
});

export default {
    oct: {
        get: () => apiOCTranspo.get(
            '/oct',
            {
                params: {
                    stopNo: 1222,
                    routeNo: 57,
                }
            },
        ),
    },
};